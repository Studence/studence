from enum import Enum

from google.protobuf.json_format import MessageToJson

from CommonQueryExecutor.GetQueryExecutor.GetQuery import GetQuery


class State(Enum):
    CHECK_ID_IS_NOT_EMPTY = 0;
    GET_FROM_DB = 1
    CONVERT_TO_UIPB = 2;
    DONE = 3;


class AGetEntityCF():
    m_getId = None;
    m_pb = None;
    m_response = None;
    m_convertor = None
    m_instance = None
    m_table = None

    def __init__(self, convertor, instance, table):
        self.m_convertor = convertor;
        self.m_instance = instance
        self.m_table = table

    def start(self, id):
        self.m_getId = id
        self.controlFlow(currentState=State.CHECK_ID_IS_NOT_EMPTY)

    def done(self):
        return self.m_response

    def checkIdIsEmpty(self):
        if (self.m_getId == None):
            assert True, "id Cannot be Empty"
            self.controlFlow(currentState=State.DONE)
        else:
            self.controlFlow(currentState=State.GET_FROM_DB)

    def getFromDb(self):
        getQuery = GetQuery(self.m_instance, self.m_table)
        self.m_pb = getQuery.get(self.m_getId)
        if (self.m_pb == None):
            raise Exception('Error while get from db ')
        else:
            self.controlFlow(currentState=State.CONVERT_TO_UIPB)

    def convertToUiPb(self):
        resp = self.m_convertor.convert(self.m_pb)
        if (resp == None):
            raise Exception('Error while Converting to Uipb ' + MessageToJson(self.m_pb))
        else:
            self.m_response = resp;
            self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        if (currentState == State.CHECK_ID_IS_NOT_EMPTY):
            self.checkIdIsEmpty()
        elif (currentState == State.GET_FROM_DB):
            self.getFromDb()
        elif (currentState == State.CONVERT_TO_UIPB):
            self.convertToUiPb()
        elif (currentState == State.DONE):
            self.done()

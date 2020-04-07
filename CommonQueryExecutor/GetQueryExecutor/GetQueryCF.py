from enum import Enum

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonQueryExecutor.GetQueryExecutor.GetQueryExecutor import GetQueryExecutor


class State(Enum):
    CHECK_ID_IS_EMPTY = 0;
    GET_FROM_DB = 1;
    CONVERT_TO_PB = 2
    DONE = 3;


class GetQueryCF():
    m_id = None
    m_pb = None;
    m_response = None;
    m_table = None
    m_instance = None

    def __init__(self, instance, table):
        self.m_table = table
        self.m_instance = instance

    m_convertToPb = ConvertJSONToPb();
    m_getQueryExecutor = GetQueryExecutor()

    def start(self, id):
        self.m_id = id
        self.controlFlow(currentState=State.CHECK_ID_IS_EMPTY)

    def done(self):
        return self.m_pb

    def checkIdIsEmpty(self):
        if (self.m_id == None):
            assert True, "id Cannot be Empty"
        else:
            self.controlFlow(currentState=State.GET_FROM_DB)

    def getFromDb(self):
        resp = self.m_getQueryExecutor.get(id=self.m_id,
                                           table=self.m_table.tableName())
        if (resp != None):
            self.m_response = resp
            self.controlFlow(currentState=State.CONVERT_TO_PB)
        else:
            # self.controlFlow(currentState=State.DONE)
            raise Exception('id NOT_FOUND ' + self.m_id)

    def convertJsonToPb(self):
        self.m_pb = self.m_convertToPb.converjsontoPBProper(response=self.m_response, instanceType=self.m_instance)
        if (self.m_pb == None):
            raise Exception('Error while Converting to Pb' + self.m_response)
        else:
            self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        if (currentState == State.CHECK_ID_IS_EMPTY):
            self.checkIdIsEmpty()
        elif (currentState == State.GET_FROM_DB):
            self.getFromDb()
        elif (currentState == State.CONVERT_TO_PB):
            self.convertJsonToPb()
        elif (currentState == State.DONE):
            self.done()

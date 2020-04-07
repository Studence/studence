from enum import Enum

from google.protobuf.json_format import MessageToJson

from CommonQueryExecutor.UpdateQueryExecutor.UpdateQuery import UpdateQuery


class State(Enum):
    CHECK_ID_IS_NOT_EMPTY = 0;
    CHECK_PB_IS_NOT_EMPTY = 1;
    CONVERT_TO_UIPB = 2
    UPDATE = 3
    DONE = 4;


class AUpdateEntityCF:
    m_getId = None;
    m_pb = None;
    m_response = None;
    m_updator = None
    m_convertor = None
    m_comparetor = None;
    m_instance = None
    m_table = None

    def __init__(self, updator, convertor, comparetor, instance, table):
        self.m_updator = updator;
        self.m_comparetor = comparetor
        self.m_convertor = convertor;
        self.m_instance = instance
        self.m_table = table

    def start(self, id, pb):
        self.m_getId = id
        self.m_pb = pb
        self.controlFlow(currentState=State.CHECK_ID_IS_NOT_EMPTY)

    def done(self):
        if (self.m_response != None):
            return self.m_pb

    def checkIdIsEmpty(self):
        if (self.m_getId == None or self.m_pb.dbInfo.id == None):
            assert True, "id Cannot be Empty"
            self.controlFlow(currentState=State.DONE)
        else:
            self.controlFlow(currentState=State.CHECK_PB_IS_NOT_EMPTY)

    def checkpbIsEmpty(self):
        if (self.m_pb == None):
            assert True, "Pb Cannot be Empty"
            self.controlFlow(currentState=State.DONE)
        else:
            self.controlFlow(currentState=State.CONVERT_TO_UIPB)

    def convertToUiPb(self):
        resp = self.m_convertor.convert(self.m_pb)
        if (resp == None):
            raise Exception('Error while Converting to Uipb ' + MessageToJson(self.m_pb))
        else:
            self.m_response = resp;
            self.controlFlow(currentState=State.UPDATE)

    def update(self):
        updateQuery = UpdateQuery(self.m_comparetor, self.m_convertor, self.m_instance, self.m_table)
        pb = updateQuery.update(id=self.m_getId, pb=self.m_response)
        if (pb == None):
            raise Exception('Error while update from db ')
        else:
            self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        if (currentState == State.CHECK_ID_IS_NOT_EMPTY):
            self.checkIdIsEmpty()
        elif (currentState == State.CHECK_PB_IS_NOT_EMPTY):
            self.checkpbIsEmpty()
        elif (currentState == State.CONVERT_TO_UIPB):
            self.convertToUiPb()
        elif (currentState == State.UPDATE):
            self.update()
        elif (currentState == State.DONE):
            self.done()

from enum import Enum

from google.protobuf.json_format import MessageToJson

from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonQueryExecutor.CreateQueryExecutor.CreateQueryExecutor import CreateQueryExecuter


class State(Enum):
    CHECK_UIPB_IS_EMPTY = 0;
    CONVERT_TO_JSON = 1;
    INSERT_TO_DB = 2
    DONE = 5;


class CreateQueryCF():
    m_pb = None;
    m_response = None;
    m_table = None

    def __init__(self,table):
        self.m_table = table

    m_convertToJson = ConvertPbToJSON();
    m_createQueryExecutor = CreateQueryExecuter()

    def start(self, m_pb):
        self.m_pb = m_pb
        self.controlFlow(currentState=State.CHECK_UIPB_IS_EMPTY)

    def done(self):
        return self.m_response

    def checkUiPbIsEmpty(self):
        if (self.m_pb == None):
            assert True, "table Name Cannot be Empty"
        else:
            self.controlFlow(currentState=State.CONVERT_TO_JSON)

    def convertToJson(self):
        self.m_response = self.m_convertToJson.converPbtojsonString(builder=self.m_pb)
        if (self.m_response != None):
            self.controlFlow(currentState=State.INSERT_TO_DB)
        else:
            #self.controlFlow(currentState=State.DONE)
            raise Exception('Convert to json Failed' + MessageToJson(self.m_pb))

    def insertInDb(self):
        resp = self.m_createQueryExecutor.create(id=self.m_pb.dbInfo.id, json=self.m_response,
                                                 table=self.m_table.tableName())
        if(resp==None):
           # self.controlFlow(currentState=State.DONE)
            raise Exception('Insert to json Failed' + MessageToJson(self.m_pb))
        else:
            self.m_response=resp
            self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        if (currentState == State.CHECK_UIPB_IS_EMPTY):
            self.checkUiPbIsEmpty()
        elif (currentState == State.CONVERT_TO_JSON):
            self.convertToJson()
        elif (currentState == State.INSERT_TO_DB):
            self.insertInDb()
        elif (currentState == State.DONE):
            self.done()

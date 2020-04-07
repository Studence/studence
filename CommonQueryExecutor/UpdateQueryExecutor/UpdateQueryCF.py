from enum import Enum

from google.protobuf.json_format import MessageToJson

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonQueryExecutor.GetQueryExecutor.GetQueryExecutor import GetQueryExecutor
from CommonQueryExecutor.UpdateQueryExecutor.UpdateQueryExecutor import UpdateQueryExecutor


class State(Enum):
    CHECK_ID_IS_EMPTY = 0;
    CHECK_PB_IS_EMPTY = 1;
    GET_FROM_DB = 2;
    CONVERT_TO_PB = 3;
    COMPARE_BOTH_PBS = 4;
    CONVERT_TO_JSON = 5;
    UPDATE_TO_DB = 6;
    DONE = 7;


class UpdateQueryCF():
    m_id = None
    m_pb = None;
    m_response = None;
    m_pbFromDb = None;
    m_json = None
    m_table = None
    m_instance = None
    m_convertor = None
    m_comparetor = None

    def __init__(self, comparetor, convertor, instance, table):
        self.m_convertor = convertor
        self.m_comparetor = comparetor
        self.m_table = table
        self.m_instance = instance

    m_convertToPb = ConvertJSONToPb();
    m_convertToJson = ConvertPbToJSON();
    m_getQueryExecutor = GetQueryExecutor()
    m_updateQueryExecutor = UpdateQueryExecutor()

    def start(self, id, pb):
        self.m_id = id
        self.m_pb = pb;
        self.controlFlow(currentState=State.CHECK_ID_IS_EMPTY)

    def done(self):
        return self.m_pb

    def checkIdIsEmpty(self):
        if (self.m_id == None):
            assert True, "id Cannot be Empty"
        else:
            self.controlFlow(currentState=State.CHECK_PB_IS_EMPTY)

    def checkPbIsEmpty(self):
        if (self.m_pb == None):
            assert True, "Pb Cannot be Empty"
        else:
            self.controlFlow(currentState=State.GET_FROM_DB)

    def getFromDb(self):
        resp = self.m_getQueryExecutor.get(id=self.m_id,
                                           table=self.m_table.tableName())
        if (resp != None):
            self.m_response = resp
            self.controlFlow(currentState=State.CONVERT_TO_PB)
        elif (self.m_pb.dbInfo.id != self.m_pbFromDb.dbInfo.id):
            raise Exception('id NOT_MATCHED you are updating wrong Entity ' + MessageToJson(self.m_pb))
        else:
            # self.controlFlow(currentState=State.DONE)
            raise Exception('id NOT_FOUND or UNEXPECTED ERROR' + self.m_id)

    def convertJsonToPb(self):
        self.m_pbFromDb = self.m_convertToPb.converjsontoPBProper(response=self.m_response,
                                                                  instanceType=self.m_instance)
        if (self.m_pbFromDb == None):
            raise Exception('Error while Converting to Pb' + self.m_response)
        else:
            self.controlFlow(currentState=State.COMPARE_BOTH_PBS)

    def comapreBothPbs(self):
        resp = self.m_comparetor.compare(newPb=self.m_pb, oldPb=self.m_pbFromDb)
        if (resp == True):
            self.controlFlow(currentState=State.CONVERT_TO_JSON)
        else:
            raise Exception('UPDATE FAILED due to improper UiPb' + MessageToJson(self.m_pb))

    def convertToJson(self):
        self.m_json = self.m_convertToJson.converPbtojsonString(builder=self.m_pb)
        if (self.m_json == None):
            raise Exception('Convert to json Failed' + MessageToJson(self.m_pb))
        else:
            self.controlFlow(currentState=State.UPDATE_TO_DB)

    def updateToDb(self):
        resp = self.m_updateQueryExecutor.update(id=self.m_id, json=self.m_json, table=self.m_table.tableName())
        if (resp == None):
            raise Exception('Update to database Failed' + MessageToJson(self.m_pb))
        else:
            self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        if (currentState == State.CHECK_ID_IS_EMPTY):
            self.checkIdIsEmpty()
        elif (currentState == State.CHECK_PB_IS_EMPTY):
            self.checkPbIsEmpty()
        elif (currentState == State.GET_FROM_DB):
            self.getFromDb()
        elif (currentState == State.CONVERT_TO_PB):
            self.convertJsonToPb()
        elif (currentState == State.COMPARE_BOTH_PBS):
            self.comapreBothPbs()
        elif (currentState == State.CONVERT_TO_JSON):
            self.convertToJson()
        elif (currentState == State.UPDATE_TO_DB):
            self.updateToDb()
        elif (currentState == State.DONE):
            self.done()

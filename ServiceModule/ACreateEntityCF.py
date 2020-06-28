from enum import Enum

from google.protobuf.json_format import MessageToJson

from BaseCodeModule.CreateEntity import CreateEntity
from CommonCode.strings import Strings
from EntityModule.EntityService import EntityService
from Protobuff.entityUiPb_pb2 import ACTIVE


class State(Enum):
    CHECK_UIPB_IS_EMPTY = 0;
    GET_ENTITY_ID = 1;
    CONVERT_TO_PB = 3;
    CREATE_IN_DB = 4
    DONE = 6;


class ACreateEntityCF:
    m_uiPb = None;
    m_id = None;
    m_response = None;
    m_json = None;
    m_updator = None

    m_entityService = EntityService()

    def __init__(self, updator, convertor, tableName, pb, updateListner):
        self.m_updator = updator;
        self.m_create = CreateEntity(convertor, tableName, pb, updateListner)

    def start(self, uipb):
        self.m_uiPb = uipb
        self.controlFlow(currentState=State.CHECK_UIPB_IS_EMPTY)

    def done(self):
        if (self.m_response != None):
            return self.m_response

    def checkUiPbIsEmpty(self):
        if (self.m_uiPb == None):
            assert True, "Uipb Cannot be Empty"
        else:
            self.controlFlow(currentState=State.GET_ENTITY_ID)

    def getEntityId(self):
        self.m_id = self.m_entityService.getEntityId()
        if (Strings.notEmpty(self.m_id)):
            self.m_uiPb.dbInfo.id = self.m_id
            self.m_uiPb.dbInfo.lifeTime = ACTIVE
            self.m_uiPb.dbInfo.version = 1
            self.controlFlow(currentState=State.CONVERT_TO_PB)
        else:
            # self.controlFlow(currentState=State.DONE)
            raise Exception('Entity id is not Genreated ')

    def convertToPb(self):
        self.m_json = self.m_updator.update(self.m_uiPb);
        if (self.m_json != None):
            self.controlFlow(currentState=State.CREATE_IN_DB)
        else:
            # self.controlFlow(currentState=State.DONE)
            raise Exception('Error while Converting to Pb' + MessageToJson(self.m_uiPb))

    def createInDb(self):
        resp = self.m_create.create(pb=self.m_json)
        if (resp == None):
            # self.controlFlow(currentState=State.DONE)
            raise Exception('Error Occur while Inserting to Db' + MessageToJson(self.m_uiPb))
        else:
            self.m_response = resp
            self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        if (currentState == State.CHECK_UIPB_IS_EMPTY):
            self.checkUiPbIsEmpty()
        elif (currentState == State.GET_ENTITY_ID):
            self.getEntityId()
        elif (currentState == State.CONVERT_TO_PB):
            self.convertToPb()
        elif (currentState == State.CREATE_IN_DB):
            self.createInDb()
        elif (currentState == State.DONE):
            self.done()

from enum import Enum

from google.protobuf.json_format import MessageToJson
from switchlang import switch

from AWSModules.SimpleDbOrpreationModule.GetOpreationInSimpleDb import GetOpreationInSimpleDb
from BaseCodeModule.GetEntity import GetEntity


class State(Enum):
    CHECK_PB_IS_EMPTY = 0
    GET_PB = 1
    COMPARE_PBS = 2
    CALL_UPDATE_LISTNER = 3
    GET_ENTITY = 4
    DONE = 5;


class UpdateEntityCF():
    m_id = None;
    m_newPb = None
    m_oldPb = None
    m_camparedPbs = None
    m_convertor = None
    m_comparetor = None
    m_getAttribute = None
    m_response = None
    m_updatelistner = None

    def __init__(self, convertor, comparetor, tableName, pb, updateListner):
        self.m_comparetor = comparetor
        self.m_convertor = convertor;
        self.m_updatelistner = updateListner
        self.m_getpb = GetOpreationInSimpleDb(tableName, pb)
        self.m_getAttribute = GetEntity(pb, convertor, tableName)

    def start(self, pb):
        self.m_newPb = pb
        self.m_newPb.dbInfo.version = self.m_newPb.dbInfo.version + 1
        self.m_id = self.m_newPb.dbInfo.id
        self.controlFlow(currentState=State.CHECK_PB_IS_EMPTY)

    def done(self):
        return self.m_response

    def checkpbisEmpty(self):
        if (self.m_newPb == None):
            raise Exception("pb is Empty")
        else:
            self.controlFlow(currentState=State.GET_PB)

    def getPb(self):
        self.m_oldPb = self.m_getpb.getAttrebute(id=self.m_id)
        if (self.m_oldPb == None):
            raise Exception("Entity not present" + self.m_id)
        else:
            self.controlFlow(currentState=State.COMPARE_PBS)

    def comparePbs(self):
        self.m_camparedPbs = self.m_comparetor.compare(self.m_newPb, self.m_oldPb)
        if (self.m_camparedPbs == None):
            raise Exception("camparedPbs not valid " + MessageToJson(self.m_newPb))
        else:
            self.controlFlow(currentState=State.CALL_UPDATE_LISTNER)

    def callUpdateListner(self):
        self.m_updatelistner.listenUpdate(self.m_camparedPbs)
        self.controlFlow(currentState=State.GET_ENTITY)

    def getEntity(self):
        self.m_response = self.m_getAttribute.getEntity(id=self.m_id)
        self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        with switch(currentState) as s:
            s.case(State.CHECK_PB_IS_EMPTY, self.checkpbisEmpty)
            s.case(State.GET_PB, self.getPb)
            s.case(State.COMPARE_PBS, self.comparePbs)
            s.case(State.CALL_UPDATE_LISTNER, self.callUpdateListner)
            s.case(State.GET_ENTITY, self.getEntity)
            s.case(State.DONE, self.done)
            s.default(self.done)

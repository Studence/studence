from enum import Enum

from switchlang import switch

from BaseCodeModule.GetEntity import GetEntity


class State(Enum):
    CHECK_PB_IS_EMPTY = 0
    CALL_UPDATE_LISTNER = 1
    GET_ENTITY = 2
    DONE = 3;


class CreateEntityCF():
    m_id = None;
    m_pb = None
    m_convertor = None
    m_getAttribute = None
    m_response = None
    m_updatelistner = None

    def __init__(self, convertor, tableName, pb, updateListner):
        self.m_convertor = convertor;
        self.m_updatelistner = updateListner
        self.m_getAttribute = GetEntity(pb, convertor, tableName)

    def start(self, pb):
        self.m_pb = pb
        self.m_id = self.m_pb.dbInfo.id
        self.controlFlow(currentState=State.CHECK_PB_IS_EMPTY)

    def done(self):
        return self.m_response

    def checkpbisEmpty(self):
        if (self.m_pb == None):
            raise Exception("pb is Empty")
        else:
            self.controlFlow(currentState=State.CALL_UPDATE_LISTNER)

    def callUpdateListner(self):
        self.m_updatelistner.listenUpdate(self.m_pb)
        self.controlFlow(currentState=State.GET_ENTITY)

    def getEntity(self):
        self.m_response = self.m_getAttribute.getEntity(id=self.m_id)
        self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        with switch(currentState) as s:
            s.case(State.CHECK_PB_IS_EMPTY, self.checkpbisEmpty)
            s.case(State.CALL_UPDATE_LISTNER, self.callUpdateListner)
            s.case(State.GET_ENTITY, self.getEntity)
            s.case(State.DONE, self.done)
            s.default(self.done)

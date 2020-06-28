from enum import Enum

from BaseCodeModule.GetEntity import GetEntity


class State(Enum):
    CHECK_ID_IS_NOT_EMPTY = 0;
    GET_FROM_DB = 1
    DONE = 3;


class AGetEntityCF():
    m_id = None;
    m_response = None;
    m_getId = None

    def __init__(self, convertor, pb, table):
        self.m_getId = GetEntity(pb,convertor,table)

    def start(self, id):
        self.m_id = id
        self.controlFlow(currentState=State.CHECK_ID_IS_NOT_EMPTY)

    def done(self):
        return self.m_response

    def checkIdIsEmpty(self):
        if (self.m_id == None):
            assert True, "id Cannot be Empty"
            self.controlFlow(currentState=State.DONE)
        else:
            self.controlFlow(currentState=State.GET_FROM_DB)

    def getFromDb(self):
        resp = self.m_getId.getEntity(id=self.m_id)
        if (resp == None):
            self.controlFlow(currentState=State.DONE)
        else:
            self.m_response = resp
            self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        if (currentState == State.CHECK_ID_IS_NOT_EMPTY):
            self.checkIdIsEmpty()
        elif (currentState == State.GET_FROM_DB):
            self.getFromDb()
        elif (currentState == State.DONE):
            self.done()

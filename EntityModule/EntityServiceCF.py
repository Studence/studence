from enum import Enum

from EntityModule.EntityQueryExecutor import EntityQueryExecuter


class State(Enum):
    GET_ENTITY = 0;
    UPDATE_ENTITY = 1
    DONE = 3;


class EntityServiceCF():
    m_response = None;
    m_queryExecutor = EntityQueryExecuter()

    def start(self):
        self.controlFlow(currentState=State.GET_ENTITY)

    def done(self):
        return self.m_response

    def getEntity(self):
        self.m_response = self.m_queryExecutor.get();
        if (self.m_response != None):
            self.controlFlow(currentState=State.UPDATE_ENTITY)
        else:
            self.controlFlow(currentState=State.GET_ENTITY);

    def updateEntity(self):
        self.m_queryExecutor.update();
        self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        if (currentState == State.GET_ENTITY):
            self.getEntity()
        elif (currentState == State.UPDATE_ENTITY):
            self.updateEntity()
        elif (currentState == State.DONE):
            self.done()

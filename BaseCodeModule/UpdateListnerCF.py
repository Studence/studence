from enum import Enum

from switchlang import switch

from EntityModule.EntityService import EntityService


class State(Enum):
    CHECK_ARGS_LIST_IS_EMPLTY = 0;
    CHECK_PB_IS_NOT_EMPTY = 1;
    CALL_CHANGE_HANDLER = 2
    DONE = 3;


class UpdateListnerCF:
    m_argsList = None;
    m_pb = None;

    m_entityService = EntityService()

    def __init__(self, argsList):
        self.m_argsList = argsList;

    def start(self, pb):
        self.m_pb = pb
        self.controlFlow(currentState=State.CHECK_ARGS_LIST_IS_EMPLTY)

    def done(self):
        return

    def checkArgsListIsEmpty(self):
        if (len(self.m_argsList) == 0):
            raise Exception("argument list is Empty")
        else:
            self.controlFlow(currentState=State.CHECK_PB_IS_NOT_EMPTY)

    def checkPbIsEmpty(self):
        if (self.m_pb == None):
            raise Exception("pb is Empty")
        else:
            self.controlFlow(currentState=State.CALL_CHANGE_HANDLER)

    def callChangeHandler(self):
        for changeObject in self.m_argsList:
            changeObject.handleChange(self.m_pb)
        self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        with switch(currentState) as s:
            s.case(State.CHECK_ARGS_LIST_IS_EMPLTY, self.checkArgsListIsEmpty)
            s.case(State.CHECK_PB_IS_NOT_EMPTY, self.checkPbIsEmpty)
            s.case(State.CALL_CHANGE_HANDLER, self.callChangeHandler)
            s.default(self.done)

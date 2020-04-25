from enum import Enum

from switchlang import switch

from AWSModules.SimpleDbModule.GetAttributeInSImpleDb import GetAttributeInSimpleDb
from CommonCode.StringToIntConvertor import StringToIntConverter
from CommonCode.intigerToStringIdConvertor import IntigerToStringIdConverter
from EntityModule.EntityPbIndexGenerator import EntityIndexPbEnum


class State(Enum):
    CHECK_ARGS_LIST_IS_EMPLTY = 0;
    GET_ENTITY = 1
    CALL_CHANGE_HANDLER = 2
    DONE = 3;


class EnityUpdateListnerCF:
    m_argsList = None;
    m_domainName = None;
    m_resp = None

    getAttribute = GetAttributeInSimpleDb()
    stringIdConvertor = IntigerToStringIdConverter()

    def __init__(self, argsList, domainName):
        self.m_argsList = argsList;
        self.m_domainName = domainName

    def start(self):
        self.controlFlow(currentState=State.CHECK_ARGS_LIST_IS_EMPLTY)

    def done(self):
        return self.stringIdConvertor.convert(int(self.m_resp))

    def checkArgsListIsEmpty(self):
        if (len(self.m_argsList) == 0):
            raise Exception("argument list is Empty")
        else:
            self.controlFlow(currentState=State.GET_ENTITY)

    def getEntity(self):
        resp = self.getAttribute.getAttributes(domainName=self.m_domainName.tableName(), id=EntityIndexPbEnum.ID.name)
        try:
            value = resp[0]
            self.m_resp = value['Value']
        except:
            self.m_resp = '0'
        self.controlFlow(currentState=State.CALL_CHANGE_HANDLER)

    def callChangeHandler(self):
        for changeObject in self.m_argsList:
            changeObject.handleChange(self.m_resp)
        self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        with switch(currentState) as s:
            s.case(State.CHECK_ARGS_LIST_IS_EMPLTY, self.checkArgsListIsEmpty)
            s.case(State.GET_ENTITY, self.getEntity)
            s.case(State.CALL_CHANGE_HANDLER, self.callChangeHandler)
            s.default(self.done)

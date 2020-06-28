from enum import Enum

from mypyc.ops import GetAttr
from switchlang import switch

from AWSModules.DynamoDbOpreationalModule.GetItemOpreationInDynamoDb import GetItemOpreationInDynamoDb
from AWSModules.SimpleDbOrpreationModule.GetOpreationInSimpleDb import GetOpreationInSimpleDb
from CommonCode.RunMainModule.RunFromMAinModule import RunFromMAinModule
from CommonCode.strings import Strings


class State(Enum):
    CHECK_ID_IS_EMPTY = 0
    GET_UIPB = 1
    DONE = 2;


class GetEntityCF():
    m_id = None;
    m_convertor = None
    m_getAttribute = None
    m_response = None

    def __init__(self, convertor, tableName, pb):
        self.m_convertor = convertor;
        self.m_getFromSimpleDb = GetOpreationInSimpleDb(tableName, pb)
        self.m_getFromDynamodb = GetItemOpreationInDynamoDb(tableName, pb)

    def start(self, id):
        self.m_id = id
        self.controlFlow(currentState=State.CHECK_ID_IS_EMPTY)

    def done(self):
        return self.m_response

    def checkIdisEmpty(self):
        if (Strings.isEmpty(self.m_id)):
            raise Exception("id is Empty")
        else:
            self.controlFlow(currentState=State.GET_UIPB)

    def getUipb(self):
        if (RunFromMAinModule().getRunFromMainModule() == True):
            self.m_response = self.m_convertor.convert(self.m_getFromSimpleDb.getAttrebute(id=self.m_id))
        else:
            self.m_response = self.m_convertor.convert(self.m_getFromDynamodb.get(id=self.m_id))
        self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        with switch(currentState) as s:
            s.case(State.CHECK_ID_IS_EMPTY, self.checkIdisEmpty)
            s.case(State.GET_UIPB, self.getUipb)
            s.case(State.DONE, self.done)
            s.default(self.done)

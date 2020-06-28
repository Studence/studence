from enum import Enum

from switchlang import switch

from AWSModules.SimpleDbModule.CreateDomainInSimpleDb import CreateDomainInSimpleDb
from AWSModules.SimpleDbOrpreationModule.SimpleDbOpreationHelper import SimpleDbOpreaTionHelper
from CommonCode.strings import Strings
from Environment.EnvironmentTypeEnum import EnvironmentTypeEnum


class State(Enum):
    CHECK_DOMAIN_NAME = 0;
    CREATE_DOMAIN = 1
    DONE = 3;


class CreateDomainInSimpleDbCF:
    m_domain_name = None;

    m_createDomian = CreateDomainInSimpleDb()
    m_simpleDbOpreationHeper = SimpleDbOpreaTionHelper()

    def start(self, domain):
        self.m_domain_name = domain
        self.controlFlow(currentState=State.CHECK_DOMAIN_NAME)

    def done(self):
        return

    def checkDominNameIsEmpty(self):
        if (Strings.isEmpty(self.m_domain_name)):
            raise Exception("domain name is Empty")
        else:
            self.controlFlow(currentState=State.CREATE_DOMAIN)

    def createDomain(self):
        for env in EnvironmentTypeEnum:
            self.m_createDomian.createDomain(
                self.m_simpleDbOpreationHeper.getTableName(tableName=self.m_domain_name, eviornment=env))

    def controlFlow(self, currentState):
        with switch(currentState) as s:
            s.case(State.CHECK_DOMAIN_NAME, self.checkDominNameIsEmpty)
            s.case(State.CREATE_DOMAIN, self.createDomain)
            s.case(State.DONE, self.done)
            s.default(self.done)

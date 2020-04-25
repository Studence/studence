from enum import Enum

from switchlang import switch

from AWSModules.SimpleDbModule.PutAttributesInSImpleDb import PutAttributesInSimpleDb
from AWSModules.SimpleDbOrpreationModule.GetOpreationInSimpleDb import GetOpreationInSimpleDb
from AWSModules.SimpleDbOrpreationModule.SimpleDbOpreationHelper import SimpleDbOpreaTionHelper


class State(Enum):
    PB_IS_EMPTY = 0
    GET_ENTITY = 2
    GENREATE_INDEX_PB = 3
    INDEX_PB = 4
    DONE = 5


class CreateOpreationInSimpleDbCF:
    m_domain_name = None;
    m_id = None
    m_pbInstance = None
    m_pb = None
    m_response = None
    m_getAttribute = None
    m_genreator = None
    m_map = None

    m_simpleDbOpreationHeper = SimpleDbOpreaTionHelper()
    m_putAttribute = PutAttributesInSimpleDb()

    def __init__(self, domain, pbInstance, genreator):
        self.m_domain_name = domain
        self.m_pbInstance = pbInstance;
        self.m_genreator = genreator;
        self.m_getAttribute = GetOpreationInSimpleDb(self.m_domain_name, self.m_pbInstance)

    def start(self, pb):
        self.m_pb = pb
        self.controlFlow(currentState=State.PB_IS_EMPTY)

    def done(self):
        return self.m_response

    def checkPbISEmpty(self):
        if (self.m_pb == None):
            raise Exception("pb is Empty")
        else:
            self.m_id = self.m_pb.dbInfo.id
            self.controlFlow(currentState=State.GENREATE_INDEX_PB)

    def genreateToIndexPb(self):
        self.m_map = self.m_genreator.genreateToPb(pb=self.m_pb)
        self.controlFlow(currentState=State.INDEX_PB)

    def indexPb(self):
        resp = self.m_putAttribute.put_attributes(id=self.m_id, domainName=self.m_domain_name.tableName(),
                                                  attributesList=self.m_simpleDbOpreationHeper.getAttributesList(
                                                      map=self.m_map))
        self.controlFlow(currentState=State.GET_ENTITY)

    def getEntity(self):
        resp = self.m_getAttribute.getAttrebute(id=self.m_id)
        if (resp == None):
            self.controlFlow(currentState=State.DONE)
        else:
            self.m_response = resp
            self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        with switch(currentState) as s:
            s.case(State.PB_IS_EMPTY, self.checkPbISEmpty)
            s.case(State.GET_ENTITY, self.getEntity)
            s.case(State.GENREATE_INDEX_PB, self.genreateToIndexPb)
            s.case(State.INDEX_PB, self.indexPb)
            s.case(State.DONE, self.done)
            s.default(self.done)

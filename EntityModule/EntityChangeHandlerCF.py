from enum import Enum

from switchlang import switch

from AWSModules.SimpleDbModule.AttributeMapper import AttributeMapper
from AWSModules.SimpleDbModule.PutAttributesInSImpleDb import PutAttributesInSimpleDb
from CommonCode.List.List import List
from CommonCode.strings import Strings
from EntityModule.EntityPbIndexGenerator import EntityPbIndexGenerator, EntityIndexPbEnum


class State(Enum):
    CHECK_ID_IS_EMPTY = 0;
    PUT_ATTRIBUTE = 1
    DONE = 3;


class EntityChangeHandlerCF:
    m_domainName = None
    m_id = None

    putAttributeIn = PutAttributesInSimpleDb()
    pbGenreator = EntityPbIndexGenerator()
    attributeMapper = AttributeMapper()

    def __init__(self, domainName):
        self.m_domainName = domainName

    def start(self, id):
        self.m_id = id
        self.controlFlow(currentState=State.CHECK_ID_IS_EMPTY)

    def done(self):
        return

    def checkIdIsEmpty(self):
        if (Strings.isEmpty(self.m_id)):
            raise Exception("id is Empty")
        else:
            self.controlFlow(currentState=State.PUT_ATTRIBUTE)

    def putAttribute(self):
        list = List()
        map = self.pbGenreator.genreateToPb(id=str(int(self.m_id) + 1))
        mapper = self.attributeMapper.mapper(name=EntityIndexPbEnum.ID.name,
                                             value=map.get_value_on_key(key=EntityIndexPbEnum.ID.name), bool=True)
        list.append(mapper)
        resp = self.putAttributeIn.put_attributes(domainName=self.m_domainName.tableName(),
                                                  id=EntityIndexPbEnum.ID.name,
                                                  attributesList=list.__list__())
        self.controlFlow(currentState=State.DONE)

    def controlFlow(self, currentState):
        with switch(currentState) as s:
            s.case(State.CHECK_ID_IS_EMPTY, self.checkIdIsEmpty)
            s.case(State.PUT_ATTRIBUTE, self.putAttribute)
            s.default(self.done)

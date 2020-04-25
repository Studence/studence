from addict import Dict

from AWSModules.DynanoDbDatabaseModule.AttributeTypeEnum import AttributeTypeEnum
from BaseCodeModule.BasicPbIndexGenreator import BasicEntityIndex
from CommonCode.List.List import List


class AttributeDefinationsMapper:
    m_config = None

    def __init__(self, config):
        self.m_config = config

    def attributeMapper(self):
        list = List()
        for element in BasicEntityIndex.list():
            mapper = Dict()
            mapper.AttributeName = element
            mapper.AttributeType = AttributeTypeEnum.S_TYPE.value
            list.__append__(mapper)

        for element in self.m_config:
            mapper = Dict()
            mapper.AttributeName = element
            mapper.AttributeType = AttributeTypeEnum.S_TYPE.value
            list.__append__(mapper)

        return list.__list__()

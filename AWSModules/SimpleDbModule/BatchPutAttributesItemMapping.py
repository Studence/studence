from addict import Dict

from CommonCode.List.List import List
from AWSModules.SimpleDbModule.AttributeMapper import AttributeMapper


class BatchPutAttributesItemMapper:
    m_attributeMapper = AttributeMapper()

    def batchAttributeItemMapper(self, itemNameList, nameList, valueList, boolList):
        m_Itemlist = List()
        for item, name, value, bool in zip(itemNameList, nameList, valueList, boolList):
            mapper = Dict()
            mapper.Name = item
            mapper.Attributes = self.m_attributeMapper.mapper(name=name, value=value, bool=bool)
            m_Itemlist.__append__(mapper)
            del mapper
        return m_Itemlist

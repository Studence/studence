from AWSModules.SimpleDbModule.AttributeMapper import AttributeMapper
from BaseCodeModule.BasicPbIndexGenreator import BasicEntityIndex
from CommonCode.List.List import List
from CommonCode.strings import Strings


class SimpleDbOpreaTionHelper:
    m_AttributeMapper = AttributeMapper()

    def getTableName(self, tableName, eviornment):
        return tableName + "_" + str(eviornment.name)

    def getAttributesList(self, map):
        list = List()
        for entry in map.entry_set():
            attribute = self.m_AttributeMapper.mapper(name=entry.key, value=str(entry.value),bool=True)
            list.__append__(attribute)
        return list.__list__()

    def getRawData(self, resp):
        for response in resp:
            if (Strings.areEquals(response['Name'], BasicEntityIndex.RAW_DATA.value)):
                return response['Value']
            else:
                continue
        return None

from addict import Dict

from AWSModules.DynanoDbDatabaseModule.AttributeTypeEnum import AttributeTypeEnum
from AWSModules.DynanoDbDatabaseModule.DynamodbKeyTypeEnum import DynamoDbKeyTypeEnum
from BaseCodeModule.BasicPbIndexGenreator import BasicEntityIndex
from CommonCode.List.List import List
from CommonCode.strings import Strings


class DynamoDbOpreationHelper:

    def getTableName(self, tableName, eviornment):
        return tableName + "_" + str(eviornment.name)

    def getAttributeList(self, m_keySchema, param, keyType):
        list = List()
        for element in m_keySchema:
            mapper = Dict()
            mapper.AttributeName = element['AttributeName']
            mapper.AttributeType = AttributeTypeEnum.S_TYPE.value
            list.__append__(mapper)
        if (keyType == DynamoDbKeyTypeEnum.RANGE_KEY):
            for element in param:
                list.__append__(element)
        return list.__list__()

    def getRawData(self, resp):
        try:
            return resp[BasicEntityIndex.RAW_DATA.name]
        except KeyError:
            return None

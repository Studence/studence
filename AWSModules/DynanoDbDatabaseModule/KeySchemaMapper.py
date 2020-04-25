from addict import Dict

from AWSModules.DynanoDbDatabaseModule.DynamodbKeyTypeEnum import DynamoDbKeyTypeEnum
from CommonCode.List.List import List


class KeySchemaMapper:

    def keyMapper(self, keyType):
        list = List()
        if keyType == DynamoDbKeyTypeEnum.HASH_KEY:
            mapper = Dict()
            list.__append__(self.getHaskKey(map=mapper))
        else:
            mapper = Dict()
            list.__append__(self.getHaskKey(map=mapper))
            list.__append__(self.getRangeKey(map=mapper))
        return list.__list__()

    def getHaskKey(self, map):
        map.AttributeName = DynamoDbKeyTypeEnum.HASH_KEY.name
        map.KeyType = DynamoDbKeyTypeEnum.HASH_KEY.value
        return map

    def getRangeKey(self, map):
        map.AttributeName = DynamoDbKeyTypeEnum.RANGE_KEY.name
        map.KeyType = DynamoDbKeyTypeEnum.RANGE_KEY.value
        return map

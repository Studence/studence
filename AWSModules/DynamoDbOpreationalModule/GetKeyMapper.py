from AWSModules.DynanoDbDatabaseModule.DynamodbKeyTypeEnum import DynamoDbKeyTypeEnum
from CommonCode.strings import Strings


class GetKeyMapper:

    def getKey(self, id, keyType):
        if (keyType == DynamoDbKeyTypeEnum.HASH_KEY):
            map = dict()
            map[DynamoDbKeyTypeEnum.HASH_KEY.name] = id
            return map
        elif (keyType == DynamoDbKeyTypeEnum.RANGE_KEY):
            key = Strings.splitString("@",id)
            map = dict()
            map[DynamoDbKeyTypeEnum.HASH_KEY.name] = key[0]
            map[DynamoDbKeyTypeEnum.RANGE_KEY.name] = key[1]
            return map

        else:
            raise Exception("Key Type is Not Exixts")

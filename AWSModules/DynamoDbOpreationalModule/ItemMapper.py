from AWSModules.DynanoDbDatabaseModule.DynamodbKeyTypeEnum import DynamoDbKeyTypeEnum
from CommonCode.HashMap.HashMap import HashMap
from CommonCode.strings import Strings
from Utitlty.ListUtility import ListUtility


class IteamMApper:
    m_listUtilty = ListUtility()

    def item_map(self, id, keyType, pbGenrated):
        map = HashMap()
        if (keyType == DynamoDbKeyTypeEnum.HASH_KEY):
            map.put(key=DynamoDbKeyTypeEnum.HASH_KEY.name, value=id)
        elif (keyType == DynamoDbKeyTypeEnum.RANGE_KEY):
            key = Strings.splitString(char="@", string=id)
            map.put(key=DynamoDbKeyTypeEnum.HASH_KEY.name, value=key[0])
            map.put(key=DynamoDbKeyTypeEnum.RANGE_KEY.name, value=key[1])

        return self.m_listUtilty.listToDict(map.entry_set(), pbGenrated.entry_set())

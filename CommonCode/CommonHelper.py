class CommonHelper:

    def getTableName(self, tableName, eviornment):
        return tableName + "_" + eviornment

    def getdbInfoId(self, hashKey, rangeKey):
        return hashKey + "@" + rangeKey

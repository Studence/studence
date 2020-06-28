from AWSModules.DynanoDbDatabaseModule.DynamodbKeyTypeEnum import DynamoDbKeyTypeEnum
from BaseCodeModule.BaseTableEntity import BaseTableEntity
from SchoolModule.SchoolConfig import SchoolConfig


class SchoolTableName(BaseTableEntity):


    def __init__(self):
        super(SchoolTableName, self).__init__(tableName=self.tableName(), keySchema=self.tableKeySchemaType(),
                                                    config=SchoolConfig.list())


    def tableName(self):
        return "SCHOOL"

    def tableKeySchemaType(self):
        return DynamoDbKeyTypeEnum.HASH_KEY

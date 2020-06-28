from AWSModules.DynanoDbDatabaseModule.DynamodbKeyTypeEnum import DynamoDbKeyTypeEnum
from BaseCodeModule.BaseTableEntity import BaseTableEntity
from ClassModule.ClassConfig import ClassConfig


class ClassTableName(BaseTableEntity):

    def __init__(self):
        super(ClassTableName, self).__init__(tableName=self.tableName(), keySchema=self.tableKeySchemaType(),
                                                    config=ClassConfig.list())

    def tableName(self):
        return "CLASS"

    def tableKeySchemaType(self):
        return DynamoDbKeyTypeEnum.HASH_KEY

from AWSModules.DynanoDbDatabaseModule.DynamodbKeyTypeEnum import DynamoDbKeyTypeEnum
from BaseCodeModule.BaseTableEntity import BaseTableEntity
from StudentModule import StudentConfig


class StudentTableName(BaseTableEntity):

    def __init__(self):
        super(StudentTableName, self).__init__(tableName=self.tableName(), keySchema=self.tableKeySchemaType(),
                                                    config=StudentConfig.list())

    def tableName(self):
        return "STUDENT"

    def tableKeySchemaType(self):
        return DynamoDbKeyTypeEnum.HASH_KEY

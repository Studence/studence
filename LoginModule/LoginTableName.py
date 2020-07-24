from AWSModules.DynanoDbDatabaseModule.DynamodbKeyTypeEnum import DynamoDbKeyTypeEnum
from BaseCodeModule.BaseTableEntity import BaseTableEntity
from LoginModule.LoginConfig import LoginConfig


class LoginTableName(BaseTableEntity):

    def __init__(self):
        super(LoginTableName, self).__init__(tableName=self.tableName(), keySchema=self.tableKeySchemaType(),
                                                    config=LoginConfig.list())

    def tableName(self):
        return "LOGIN"

    def tableKeySchemaType(self):
        return DynamoDbKeyTypeEnum.RANGE_KEY

from AWSModules.DynanoDbDatabaseModule.DynamodbKeyTypeEnum import DynamoDbKeyTypeEnum
from BaseCodeModule.BaseTableEntity import BaseTableEntity
from LoginModule.LoginConfig import LoginConfig


class AttendanceTableName(BaseTableEntity):

    def __init__(self):
        super(AttendanceTableName, self).__init__(tableName=self.tableName(), keySchema=self.tableKeySchemaType(),
                                                    config=LoginConfig.list())

    def tableName(self):
        return "ATTENDANCE"

    def tableKeySchemaType(self):
        return DynamoDbKeyTypeEnum.RANGE_KEY

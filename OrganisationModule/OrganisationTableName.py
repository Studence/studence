from AWSModules.DynanoDbDatabaseModule.DynamodbKeyTypeEnum import DynamoDbKeyTypeEnum
from BaseCodeModule.BasicTableEntity import BasicTableEntity
from OrganisationModule.OrganisationConfig import OrganisationConfig


class OrganisationTableName(BasicTableEntity):

    def __init__(self):
        super(OrganisationTableName, self).__init__(tableName=self.tableName(), keySchema=self.tableKeySchemaType(),
                                                    config=OrganisationConfig.list())

    def tableName(self):
        return "ORGANISATION"

    def tableKeySchemaType(self):
        return DynamoDbKeyTypeEnum.HASH_KEY

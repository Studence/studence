from AWSModules.DynamoDbOpreationalModule.CreateTableOpreationInDynamodb import CreateTableOpreationInDynamodb
from AWSModules.SimpleDbOrpreationModule.CreateDomainInSimpleDb import CreateDomainInSimpleDb


class BaseTableEntity(CreateDomainInSimpleDb, CreateTableOpreationInDynamodb):

    def __init__(self, tableName, keySchema, config):
        CreateDomainInSimpleDb.__init__(self=self,tableName=tableName)
        CreateTableOpreationInDynamodb.__init__(self=self,tableName=tableName, keyType=keySchema, config=config)

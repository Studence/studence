from AWSModules.DynanoDbDatabaseModule.DynamoDbConnection import DynamoDbConnection


class CreateTableInDynamoDb(DynamoDbConnection):

    def createTable(self, tableName, keySchemaList, AttributeDefinitionList):
        try:
            self.getConnection().create_table(
                TableName=tableName,
                KeySchema=keySchemaList,
                AttributeDefinitions=AttributeDefinitionList,
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
        except:
            pass

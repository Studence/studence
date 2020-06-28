from AWSModules.DynamoDbOpreationalModule.DynamoDbOpreationHelper import DynamoDbOpreationHelper
from AWSModules.DynanoDbDatabaseModule.DynamoDbConnection import DynamoDbConnection
from AWSModules.DynanoDbDatabaseModule.DynamoDbResponseJsonParser import DynamodbResponseJsonParser
from Environment.ServerListner import ServerListner


class PutItemInDynamodb(DynamoDbConnection):
    m_serverListner = ServerListner()
    m_commonHelper = DynamoDbOpreationHelper()
    m_responseParser = DynamodbResponseJsonParser()

    def put_item(self, tableName, item):
        resp = self.m_responseParser.parseJson(
            response=self.getConnection().Table(self.m_commonHelper.getTableName(tableName=tableName,
                                                                                 eviornment=self.m_serverListner.getServerEnvironment())).put_item(
                Item=item
            ))
        resp = resp['ResponseMetadata']
        if (resp["HTTPStatusCode"] == 200):
            return
        else:
            raise Exception("Dynamodb Response is Not Valid Or Failed")

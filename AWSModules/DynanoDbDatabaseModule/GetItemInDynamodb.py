from AWSModules.DynamoDbOpreationalModule.DynamoDbOpreationHelper import DynamoDbOpreationHelper
from AWSModules.DynanoDbDatabaseModule.DynamoDbConnection import DynamoDbConnection
from AWSModules.DynanoDbDatabaseModule.DynamoDbResponseJsonParser import DynamodbResponseJsonParser
from Environment.ServerListner import ServerListner


class GetItemInDynamodb(DynamoDbConnection):
    m_serverListner = ServerListner()
    m_commonHelper = DynamoDbOpreationHelper()
    m_responseParser = DynamodbResponseJsonParser()

    def get_item(self, tableName, key):
        resp = self.getConnection().Table(self.m_commonHelper.getTableName(tableName=tableName,
                                                                           eviornment=self.m_serverListner.getServerEnvironment())).get_item(
            Key=key
        )
        httpsResp = resp['ResponseMetadata']
        if (httpsResp["HTTPStatusCode"] == 200):
            try:
                return resp['Item']
            except KeyError:
                return None
        else:
            raise Exception("SimpleDB Response is Not Valid Or Failed")

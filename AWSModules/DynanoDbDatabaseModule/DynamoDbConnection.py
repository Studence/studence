import boto3

from AWSModules.AWSCredential import AWSCredential
from AWSModules.DynanoDbDatabaseModule.DynamodbEndPointUrl import DynamodbEndPointUrl


class DynamoDbConnection:
    m_credentials = AWSCredential()
    m_endpointUrl = DynamodbEndPointUrl()

    def getConnection(self):
        return boto3.resource('dynamodb', region_name='ap-south-1', aws_access_key_id=self.m_credentials.getAccessKey(),
                              aws_secret_access_key=self.m_credentials.getAccessSecretKey(),
                              endpoint_url="http://localhost:8000")

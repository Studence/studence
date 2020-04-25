import boto3

from AWSModules.AWSCredential import AWSCredential
from AWSModules.SimpleDbModule.SimpleDbEndPointUrl import SimpleDbEndPointUrl


class SimpleDbConnection:
    m_credentials = AWSCredential()
    m_endpointUrl = SimpleDbEndPointUrl()

    def getConnection(self):
        return boto3.client('sdb', region_name='ap-south-1', aws_access_key_id=self.m_credentials.getAccessKey(),
                              aws_secret_access_key=self.m_credentials.getAccessSecretKey(),
                              endpoint_url="http://localhost:3333")

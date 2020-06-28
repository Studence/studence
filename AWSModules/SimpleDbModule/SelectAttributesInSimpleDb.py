from AWSModules.SimpleDbModule.SimpleDbConnection import SimpleDbConnection
from AWSModules.SimpleDbModule.SimpleDbResponseJsonParser import SimpleDbResponseJsonParser
from CommonCode.CommonHelper import CommonHelper
from Environment.ServerListner import ServerListner


class SelectAttributesInSimpleDb(SimpleDbConnection):
    m_serverListner = ServerListner()
    m_commonHelper = CommonHelper()
    m_responseParser = SimpleDbResponseJsonParser()

    def put_attributes(self, id, query, nextToken):
        if (nextToken == None):
            resp = self.m_responseParser.parseJson(response=self.getConnection().client.select(
                SelectExpression=query
            ))
        else:
            resp = self.m_responseParser.parseJson(response=self.getConnection().client.select(
                SelectExpression=query,
                NextToken=nextToken
            ))

        if (resp["HTTPStatusCode"] != 200):
            return resp['Items']
        else:
            raise Exception("SimpleDB Response is Not Valid Or Success")

from AWSModules.SimpleDbOrpreationModule.SimpleDbOpreationHelper import SimpleDbOpreaTionHelper
from CommonCode.CommonHelper import CommonHelper
from Environment.ServerListner import ServerListner
from AWSModules.SimpleDbModule.SimpleDbConnection import SimpleDbConnection
from AWSModules.SimpleDbModule.SimpleDbResponseJsonParser import SimpleDbResponseJsonParser


class GetAttributeInSimpleDb(SimpleDbConnection):
    m_serverListner = ServerListner()
    m_commonHelper = SimpleDbOpreaTionHelper()
    m_responseParser = SimpleDbResponseJsonParser()

    def getAttributes(self, domainName, id):
        resp = self.m_responseParser.parseJson(response=self.getConnection().get_attributes(
            DomainName=self.m_commonHelper.getTableName(domainName, self.m_serverListner.getServerEnvironment()),
            ItemName=id
        ))
        httpsResp = resp['ResponseMetadata']
        if (httpsResp["HTTPStatusCode"] == 200):
            try:
                return resp['Attributes']
            except KeyError:
                return None
        else:
            raise Exception("SimpleDB Response is Not Valid Or Failed")

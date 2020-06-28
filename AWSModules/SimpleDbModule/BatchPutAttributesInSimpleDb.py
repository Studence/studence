from CommonCode.CommonHelper import CommonHelper
from Environment.ServerListner import ServerListner
from AWSModules.SimpleDbModule.SimpleDbConnection import SimpleDbConnection
from AWSModules.SimpleDbModule.SimpleDbResponseJsonParser import SimpleDbResponseJsonParser


class BatchPutAttrabutesInSimplaeDb(SimpleDbConnection):
    m_serverListner = ServerListner()
    m_commonHelper = CommonHelper()
    m_responseParser = SimpleDbResponseJsonParser()

    def batchPutAttributes(self, domainName, itemList):
        resp = self.m_responseParser.parseJson(response=self.getConnection().client.get_attributes(
            DomainName=str(
                self.m_commonHelper.getTableName(domainName, self.m_serverListner.getServerEnvironment().name)),
            Items=itemList
        ))
        if (resp["HTTPStatusCode"] != 200):
            return
        else:
            raise Exception("SimpleDB Response is Not Valid Or Success")

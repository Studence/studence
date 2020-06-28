from AWSModules.SimpleDbModule.SimpleDbConnection import SimpleDbConnection
from AWSModules.SimpleDbModule.SimpleDbResponseJsonParser import SimpleDbResponseJsonParser


class ListDomainInSimpleDb(SimpleDbConnection):
    m_responseParser = SimpleDbResponseJsonParser()

    def listDomain(self):
        resp = self.m_responseParser.parseJson(response=self.getConnection().client.list_domains(
        ))
        if (resp["HTTPStatusCode"] != 200):
            return resp["DomainNames"]
        else:
            raise Exception("SimpleDB Response is Not Valid Or Success")

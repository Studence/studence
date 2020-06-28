from AWSModules.SimpleDbModule.SimpleDbConnection import SimpleDbConnection
from AWSModules.SimpleDbModule.SimpleDbResponseJsonParser import SimpleDbResponseJsonParser


class CreateDomainInSimpleDb(SimpleDbConnection):
    m_responseParser = SimpleDbResponseJsonParser()

    def createDomain(self, domainName):
        resp = self.m_responseParser.parseJson(response=self.getConnection().create_domain(
            DomainName=domainName
        ))
        obj = resp['ResponseMetadata']
        if (obj['HTTPStatusCode'] == 200):
            return
        else:
            raise Exception("SimpleDB Response is Not Valid Or Success")

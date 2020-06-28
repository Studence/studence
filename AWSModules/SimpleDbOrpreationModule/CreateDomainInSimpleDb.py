from AWSModules.SimpleDbOrpreationModule.CreateDomainInSimpleDbCF import CreateDomainInSimpleDbCF


class CreateDomainInSimpleDb:
    m_tableName = None

    def __init__(self, tableName):
        self.m_tableName = tableName
        self.createDomain()

    def createDomain(self):
        createDomainInSimpleDbCF = CreateDomainInSimpleDbCF()
        createDomainInSimpleDbCF.start(domain=self.m_tableName)
        return createDomainInSimpleDbCF.done()

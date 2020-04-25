from AWSModules.SimpleDbOrpreationModule.CreateOpreationInSimpleDbCF import CreateOpreationInSimpleDbCF


class CreateOpreationInSimpleDb:
    m_pbInstance = None
    m_domainName = None
    m_generator = None

    def __init__(self, domainName, pbInstance, generator):
        self.m_pbInstance = pbInstance
        self.m_domainName = domainName
        self.m_generator = generator

    def putAttribute(self, pb):
        createOpreationInSimpleDbCF = CreateOpreationInSimpleDbCF(self.m_domainName, self.m_pbInstance,
                                                                  self.m_generator)
        createOpreationInSimpleDbCF.start(pb=pb);
        return createOpreationInSimpleDbCF.done()

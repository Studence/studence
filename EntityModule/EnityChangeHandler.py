from EntityModule.EntityChangeHandlerCF import EntityChangeHandlerCF


class EntityChangeHandler:
    m_domainName = None

    def __init__(self, domainName):
        self.m_domainName = domainName

    def handleChange(self, id):
        entityChangeHandlerCF = EntityChangeHandlerCF(self.m_domainName)
        entityChangeHandlerCF.start(id=id)
        entityChangeHandlerCF.done()

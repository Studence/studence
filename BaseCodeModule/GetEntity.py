from BaseCodeModule.GetEntityCF import GetEntityCF


class GetEntity:
    m_domainName = None;
    m_pbInsatance = None;
    m_convertor = None

    def __init__(self, pb, convertor, domainName):
        self.m_pbInsatance = pb;
        self.m_domainName = domainName
        self.m_convertor = convertor

    def getEntity(self, id):
        get = GetEntityCF(self.m_convertor, self.m_domainName, self.m_pbInsatance)
        get.start(id=id)
        return get.done()

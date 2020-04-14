from ServiceModule.AUpdateEntityCF import AUpdateEntityCF


class AUpdateEntity:
    m_updator = None
    m_convertor = None
    m_comparetor = None;
    m_instance = None
    m_table = None

    def __init__(self, updator, convertor, comparetor, instance, table):
        self.m_updator = updator;
        self.m_comparetor = comparetor
        self.m_convertor = convertor;
        self.m_instance = instance
        self.m_table = table

    def update(self, id, uipb):
        m_aUpdateEntity = AUpdateEntityCF(self.m_updator, self.m_convertor, self.m_comparetor,
                                        self.m_instance, self.m_table)
        m_aUpdateEntity.start(id=id, pb=uipb)
        return m_aUpdateEntity.done()

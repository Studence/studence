from ServiceModule.AUpdateEntityCF import AUpdateEntityCF


class AUpdateEntity:
    m_updator = None
    m_convertor = None
    m_comparetor = None;
    m_pbinstance = None
    m_table = None
    m_updateListner = None

    def __init__(self, updator, convertor, comparetor, pbinstance, table, updateListner):
        self.m_updator = updator;
        self.m_comparetor = comparetor
        self.m_convertor = convertor;
        self.m_pbinstance = pbinstance
        self.m_updateListner = updateListner
        self.m_table = table

    def update(self, id, uipb):
        m_aUpdateEntity = AUpdateEntityCF(self.m_updator, self.m_convertor, self.m_comparetor,
                                          self.m_pbinstance, self.m_table, self.m_updateListner)
        m_aUpdateEntity.start(id=id, pb=uipb)
        return m_aUpdateEntity.done()

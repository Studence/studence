from ServiceModule.ACreateEntityCF import ACreateEntityCF


class ACreateEntity:
    m_updator = None
    m_instance = None
    m_table = None
    m_convertor = None
    m_updatelistner = None

    def __init__(self, updator, convertor, pb, updateListner, tableName):
        self.m_updator = updator;
        self.m_convertor = convertor
        self.m_instance = pb;
        self.m_table = tableName;
        self.m_updatelistner = updateListner

    def create(self, uipb):
        m_aCreateEnity = ACreateEntityCF(self.m_updator, self.m_convertor, self.m_table, self.m_instance,
                                         self.m_updatelistner)
        m_aCreateEnity.start(uipb=uipb)
        if (m_aCreateEnity.done() == None):
            raise Exception('Entity not created')
        else:
            return m_aCreateEnity.done()

from ServiceModule.ACreateEntityCF import ACreateEntityCF


class ACreateEntity:
    m_updator = None
    m_instance = None
    m_table = None
    m_convertor = None

    def __init__(self, updator, convertor, pb, table):
        self.m_updator = updator;
        self.m_convertor = convertor
        self.m_instance = pb;
        self.m_table = table;

    def create(self, uipb):
        m_aCreateEnity = ACreateEntityCF(self.m_updator, self.m_convertor, self.m_instance, self.m_table)
        m_aCreateEnity.start(uipb=uipb)
        if (m_aCreateEnity.done() == None):
            raise Exception('Entity not created')
        else:
            return m_aCreateEnity.done()

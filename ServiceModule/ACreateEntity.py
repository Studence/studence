from ServiceModule.ACreateEntityCF import ACreateEntityCF


class ACreateEntity:
    m_updator = None
    m_uipb = None
    m_table = None

    def __init__(self, updator, uipb, table):
        self.m_updator = updator;
        self.m_instance = uipb;
        self.m_table = table;

    def create(self, uipb):
        m_aCreateEnity = ACreateEntityCF(self.m_updator, self.m_uipb, self.m_table)
        m_aCreateEnity.start(uipb=uipb)
        return m_aCreateEnity.done()

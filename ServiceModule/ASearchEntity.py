from ServiceModule.ASearchEntityCF import ASearchEntityCF


class ASearchEntity:
    m_searcher = None;
    m_responseUipb = None
    m_instance = None
    m_table = None

    def __init__(self, searcher, responseUipb, instance, table):
        self.m_responseUipb = responseUipb;
        self.m_searcher = searcher
        self.m_instance = instance
        self.m_table = table

    def search(self, reqUipb):
        m_aSearchEntitycf = ASearchEntityCF(self.m_searcher, self.m_responseUipb, self.m_instance, self.m_table)
        m_aSearchEntitycf.start(reqUipb=reqUipb)
        return m_aSearchEntitycf.done()

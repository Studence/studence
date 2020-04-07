from ServiceModule.AGetEntityCF import AGetEntityCF


class AGetEntity:
    m_convertor = None
    m_instance = None
    m_table = None

    def __init__(self, convertor, instance, table):
        self.m_convertor = convertor;
        self.m_instance = instance
        self.m_table = table

    def get(self, id):
        m_aGetEntity = AGetEntityCF(self.m_convertor, self.m_instance, self.m_table)
        m_aGetEntity.start(id=id)
        return m_aGetEntity.done()

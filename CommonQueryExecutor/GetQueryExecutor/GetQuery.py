from CommonQueryExecutor.GetQueryExecutor.GetQueryCF import GetQueryCF


class GetQuery:
    m_table = None;
    m_instance = None

    def __init__(self, instance, table):
        self.m_table = table
        self.m_instance = instance

    def get(self, id):
        getQuerycf = GetQueryCF(self.m_instance, self.m_table);
        getQuerycf.start(id=id)
        return getQuerycf.done();

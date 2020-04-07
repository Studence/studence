from CommonQueryExecutor.CreateQueryExecutor.CreateQueryCF import CreateQueryCF


class CreateQuery:
    m_table = None;

    def __init__(self, table):
        self.m_table = table

    def create(self, pb):
        createQuerycf = CreateQueryCF(self.m_table);
        createQuerycf.start(m_pb=pb)
        return createQuerycf.done();

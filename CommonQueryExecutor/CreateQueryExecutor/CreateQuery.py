from CommonQueryExecutor.CreateQueryExecutor.CreateQueryCF import CreateQueryCF


class CreateQuery:
    m_table = None;
    m_instance = None

    def __init__(self, instance, table):
        self.m_table = table
        self.m_instance = instance

    def create(self, pb):
        createQuerycf = CreateQueryCF(self.m_instance, self.m_table);
        createQuerycf.start(m_pb=pb)
        if (createQuerycf.done() == None):
            raise Exception('Entity not created')
        else:
            return createQuerycf.done()

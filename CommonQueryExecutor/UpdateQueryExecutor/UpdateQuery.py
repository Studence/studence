from CommonQueryExecutor.UpdateQueryExecutor.UpdateQueryCF import UpdateQueryCF


class UpdateQuery:
    m_table = None;
    m_instance = None
    m_comparetor = None
    m_convertor = None

    def __init__(self, comparetor, convertor, instance, table):
        self.m_comparetor = comparetor
        self.m_convertor = convertor
        self.m_table = table
        self.m_instance = instance

    def update(self, id, pb):
        updateQuerycf = UpdateQueryCF(self.m_comparetor, self.m_convertor, self.m_instance, self.m_table);
        updateQuerycf.start(id=id, pb=pb)
        if (updateQuerycf.done() == None):
            raise Exception('Entity not Updated')
        else:
            return updateQuerycf.done();

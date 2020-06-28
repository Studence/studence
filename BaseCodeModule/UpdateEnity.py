from BaseCodeModule.UpdateEntityCF import UpdateEntityCF


class UpdateEntity:
    m_convertor = None
    m_updatelistner = None
    m_tableName = None
    m_pbInstance = None
    m_comparetor = None

    def __init__(self, comparetor, convertor, tableName, pb, updateListner):
        self.m_comparetor = comparetor
        self.m_convertor = convertor;
        self.m_updatelistner = updateListner
        self.m_tableName = tableName
        self.m_pbInstance = pb

    def update(self, pb):
        updatecf = UpdateEntityCF(self.m_convertor, self.m_comparetor, self.m_tableName, self.m_pbInstance,
                                  self.m_updatelistner)
        updatecf.start(pb=pb)
        return updatecf.done()

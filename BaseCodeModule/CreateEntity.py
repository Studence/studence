from BaseCodeModule.CreateEntityCF import CreateEntityCF


class CreateEntity:
    m_convertor = None
    m_updatelistner = None
    m_tableName = None
    m_pbInstance = None

    def __init__(self, convertor, tableName, pb, updateListner):
        self.m_convertor = convertor;
        self.m_updatelistner = updateListner
        self.m_tableName = tableName
        self.m_pbInstance = pb

    def create(self, pb):
        createcf = CreateEntityCF(self.m_convertor, self.m_tableName, self.m_pbInstance, self.m_updatelistner)
        createcf.start(pb=pb)
        return createcf.done()

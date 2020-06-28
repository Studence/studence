from AWSModules.SimpleDbOrpreationModule.GetOpreationInSimpleDbCF import GetOpreationInSimpleDbCF


class GetOpreationInSimpleDb:
    m_tableName = None
    m_pb = None

    def __init__(self, tableName, pb):
        self.m_tableName = tableName
        self.m_pb = pb

    def getAttrebute(self, id):
        getOpreationInSimpleDbcf = GetOpreationInSimpleDbCF(self.m_tableName, self.m_pb)
        getOpreationInSimpleDbcf.start(id=id)
        return getOpreationInSimpleDbcf.done()

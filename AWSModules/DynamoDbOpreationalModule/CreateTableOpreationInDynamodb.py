from AWSModules.DynamoDbOpreationalModule.CreateTableOpreationInDynamodbCF import CreateTableOpreationInDynamodbCF


class CreateTableOpreationInDynamodb:
    m_tableName = None
    m_Keytype = None
    m_config = None

    def __init__(self, tableName, keyType, config):
        self.m_tableName = tableName
        self.m_Keytype = keyType
        self.m_config = config
        self.createTable()

    def createTable(self):
        m_createcf = CreateTableOpreationInDynamodbCF(self.m_Keytype, self.m_config)
        m_createcf.start(tableName=self.m_tableName)
        return m_createcf.done()

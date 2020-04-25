from AWSModules.DynamoDbOpreationalModule.CreateItemOpreationInDynamoDbCF import CreateItemOpreationInDynamoDbCF


class CreateItemOpreationInDynamoDb:
    m_table_name = None
    m_pbInstance = None
    m_genreator = None

    def __init__(self, table, pbInstance, genreator):
        self.m_table_name = table
        self.m_pbInstance = pbInstance;
        self.m_genreator = genreator;

    def put_item(self, pb):
        createOrUpdate = CreateItemOpreationInDynamoDbCF(self.m_table_name, self.m_pbInstance, self.m_genreator)
        createOrUpdate.start(pb=pb)
        return createOrUpdate.done()

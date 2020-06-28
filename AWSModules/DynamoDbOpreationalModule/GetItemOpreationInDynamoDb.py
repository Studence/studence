from AWSModules.DynamoDbOpreationalModule.GetItemOpreationInDynamoDbCF import GetItemOpreationInDynamoDbCF


class GetItemOpreationInDynamoDb:
    m_table = None
    m_pbInstance = None

    def __init__(self, table, pbInstance):
        self.m_table = table
        self.m_pbInstance = pbInstance

    def get(self, id):
        getcf = GetItemOpreationInDynamoDbCF(self.m_table, self.m_pbInstance)
        getcf.start(id=id)
        return getcf.done()

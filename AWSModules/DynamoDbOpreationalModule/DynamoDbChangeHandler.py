from AWSModules.DynamoDbOpreationalModule.CreateItemOpreationInDynamoDb import CreateItemOpreationInDynamoDb


class DynamoDbChangeHandler(CreateItemOpreationInDynamoDb):

    def __init__(self, domainName, pb, genreator):
        super(DynamoDbChangeHandler, self).__init__(domainName, pb, genreator)

    def handleChange(self, pb):
        self.put_item(pb=pb)

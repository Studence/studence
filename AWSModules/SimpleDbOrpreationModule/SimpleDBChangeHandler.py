from AWSModules.SimpleDbOrpreationModule.CreateOpreationInSimpleDb import CreateOpreationInSimpleDb


class SimpleDbChangeHandler(CreateOpreationInSimpleDb):

    def __init__(self, domainName, pb, gereator):
        super(SimpleDbChangeHandler, self).__init__(domainName, pb, gereator)

    def handleChange(self, pb):
        self.putAttribute(pb=pb)

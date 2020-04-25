from AWSModules.SimpleDbOrpreationModule.CreateDomainInSimpleDb import CreateDomainInSimpleDb


class EntityTableName(CreateDomainInSimpleDb):
    def __init__(self):
        super(EntityTableName, self).__init__(tableName=self.tableName())

    def tableName(self):
        return "ENTITY"

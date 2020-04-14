from PostgreSQLDatabase.CheckTableExixtsOrNot import CheckTableExixtsOrNot


class ClassTableName:
    m_checkTableExixts = CheckTableExixtsOrNot();

    def __init__(self):
        self.m_checkTableExixts.checkTableExixts(tableName=self.tableName())

    def tableName(self):
        return "CLASS"

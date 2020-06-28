from CommonCode.strings import Strings
from Environment.EnvironmentTypeEnum import EnvironmentTypeEnum
from PostgreSQLDatabase.CreateEntityTableDb import CreateEntityTableDb
from PostgreSQLDatabase.CreateTableInDb import CreateTableInDb
from PostgreSQLDatabase.PostgreSqlDataBaseConnection import PostgreSQLDatabaseConnection


class CheckTableExixtsOrNot:
    m_createTable = CreateTableInDb()
    m_createEntiyTable = CreateEntityTableDb()
    m_databaseConnection = PostgreSQLDatabaseConnection()

    def checkTableExixts(self, tableName):
        if (self.checkTable(tableName)):
            return True;
        else:
            if (Strings.areEquals(tableName, "ENTITY")):
                self.m_createEntiyTable.createTable(tableName=tableName)
            else:
                self.m_createTable.createTable(tableName=tableName)

    def checkTable(self, tableName):
        assert Strings.notEmpty(tableName), "table Name Cannot be Empty"
        connection = self.m_databaseConnection.getConnection()
        cursor = connection.cursor()
        check = False;
        for env in EnvironmentTypeEnum:
            try:
                query = self.ckeckTableQuery(tableName=Strings.concatinateWithUnderScore(str1=tableName, str2=env.name))
                print(query)
                cursor.execute(query)
                val = cursor.fetchall()[0]
                check = val[0]
                connection.commit()
            except:
                pass
        self.m_databaseConnection.closeConnection(connection=connection);
        if (check):
            return check;

    def ckeckTableQuery(self, tableName):
        return "SELECT EXISTS ( SELECT 1 FROM pg_tables WHERE schemaname = 'public' AND tablename = '" + tableName + "' );"

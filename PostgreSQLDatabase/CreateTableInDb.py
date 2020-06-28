from itertools import takewhile

from CommonCode.strings import Strings
from Environment.EnvironmentTypeEnum import EnvironmentTypeEnum
from PostgreSQLDatabase.PostgreSqlDataBaseConnection import PostgreSQLDatabaseConnection


class CreateTableInDb:
    m_databaseConnection = PostgreSQLDatabaseConnection()

    def createTable(self, tableName):
        assert Strings.notEmpty(tableName), "table Name Cannot be Empty"
        connection = self.m_databaseConnection.getConnection()
        for env in EnvironmentTypeEnum:
            try:
                query = self.getCreateTableQuery(table=Strings.concatinateWithUnderScore(str1=tableName, str2=env.name))
                print(query)
                connection.cursor().execute(query)
                connection.commit()
            except:
                pass
        self.m_databaseConnection.closeConnection(connection=connection);

    def getCreateTableQuery(self, table):
        return 'CREATE TABLE' + '"' + table + '"' + '(id serial PRIMARY KEY,dbid VARCHAR (255) UNIQUE NOT NULL,raw_data json NOT NULL);'

from itertools import takewhile

import psycopg2

from CommonCode.strings import Strings
from Environment.EnvironmentTypeEnum import EnvironmentTypeEnum
from PostgreSQLDatabase.PostgreSqlDataBaseConnection import PostgreSQLDatabaseConnection


class CreateEntityTableDb:
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
                query = self.insertQuery(table=Strings.concatinateWithUnderScore(str1=tableName, str2=env.name))
                print(query)
                connection.cursor().execute(query)
                connection.commit()
            except (Exception, psycopg2.Error) as error:
                print(error)
        self.m_databaseConnection.closeConnection(connection=connection);

    def getCreateTableQuery(self, table):
        return 'CREATE TABLE ' + '"' + table + '"' + ' (id serial PRIMARY KEY,dbid VARCHAR (255) UNIQUE NOT NULL);'

    def insertQuery(self, table):
        return 'INSERT INTO ' + '"' + table + '"' + ' (dbid) VALUES ('+"'"+'1'+"'"+');'

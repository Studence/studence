import psycopg2

from CommonCode.strings import Strings
from Environment.ServerListner import ServerListner
from PostgreSQLDatabase.PostgreSqlDataBaseConnection import PostgreSQLDatabaseConnection


class CreateQueryExecuter:
    m_dbConnection = PostgreSQLDatabaseConnection()
    m_serverListner = ServerListner()

    def create(self, id, json, table):
        try:
            query = self.getCreateQuery(id=id, table=Strings.concatinateWithUnderScore(str1=table,
                                                                                       str2=self.m_serverListner.getServerEnvironment().name),
                                        data=json)
            print(query)
            conn = self.m_dbConnection.getConnection()
            cursor = conn.cursor()
            cursor.execute(query)
            if (cursor.rowcount == 1):
                conn.commit()
                conn.close()
                conn.close()
                return json
            else:
                conn.commit()
                conn.close()
                conn.close()
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

    def getCreateQuery(self, id, table, data):
        return 'INSERT INTO "' + table + '"' + "( dbid , raw_data) " + " VALUES " + "(" + Strings.qoutedString(
            id) + " , " + data + ");"

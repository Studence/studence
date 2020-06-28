import psycopg2

from CommonCode.strings import Strings
from Environment.ServerListner import ServerListner
from PostgreSQLDatabase.PostgreSqlDataBaseConnection import PostgreSQLDatabaseConnection


class GetQueryExecutor:
    m_dbConnection = PostgreSQLDatabaseConnection()
    m_serverListner = ServerListner()

    def get(self, id, table):
        try:
            query = self.getQuery(table=Strings.concatinateWithUnderScore(str1=table,
                                                                          str2=self.m_serverListner.getServerEnvironment().name),
                                  id=id)
            print(query)
            conn = self.m_dbConnection.getConnection()
            cursor = conn.cursor()
            cursor.execute(query)
            if (cursor.rowcount == 1):
                row = cursor.fetchall()
                data = row[0]
                conn.commit()
                conn.close()
                cursor.close()
                return data[0]
            else:
                conn.commit()
                conn.close()
                cursor.close()
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

    def getQuery(self, table, id):
        return 'SELECT raw_data from  "' + table + '"' + " WHERE dbid = " + Strings.qoutedString(id) + ";"

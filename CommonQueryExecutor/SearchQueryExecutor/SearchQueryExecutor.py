import psycopg2

from CommonCode.strings import Strings
from Environment.ServerListner import ServerListner
from PostgreSQLDatabase.PostgreSqlDataBaseConnection import PostgreSQLDatabaseConnection


class SearchQueryExecutor:
    m_dbConnection = PostgreSQLDatabaseConnection()
    m_serverListner = ServerListner()

    def search(self, query, table):
        try:
            query = self.getSearchQuery(table=Strings.concatinateWithUnderScore(str1=table,
                                                                                str2=self.m_serverListner.getServerEnvironment().name),
                                        subquery=query)
            print(query)
            conn = self.m_dbConnection.getConnection()
            cursor = conn.cursor()
            cursor.execute(query)
            if (cursor.rowcount > 0):
                row = cursor.fetchall()
                conn.commit()
                conn.close()
                cursor.close()
                return row
            else:
                conn.commit()
                conn.close()
                cursor.close()
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

    def getSearchQuery(self, table, subquery):
        return 'SELECT raw_data FROM "' + table + '" WHERE ' + subquery + ';'

import psycopg2

from CommonCode.strings import Strings
from Environment.ServerListner import ServerListner
from PostgreSQLDatabase.PostgreSqlDataBaseConnection import PostgreSQLDatabaseConnection


class UpdateQueryExecutor:
    m_dbConnection = PostgreSQLDatabaseConnection()
    m_serverListner = ServerListner()

    def update(self, id, json, table):
        try:
            query = self.getUpdateQuery(id=id, json=json, table=Strings.concatinateWithUnderScore(str1=table,
                                                                                                  str2=self.m_serverListner.getServerEnvironment().name))
            print(query)
            conn = self.m_dbConnection.getConnection()
            cursor = conn.cursor()
            cursor.execute(str(query))
            if (cursor.rowcount > 0):
                conn.commit()
                conn.close()
                cursor.close()
                return json
            else:
                conn.commit()
                conn.close()
                cursor.close()
                return None
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

    def getUpdateQuery(self, id, json, table):
        return 'UPDATE "' + table + '"' + " SET raw_data = " + json + " WHERE dbid = " + Strings.qoutedString(id) + " ;"

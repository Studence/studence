import psycopg2

from CommonCode.intigerToStringIdConvertor import IntigerToStringIdConverter
from CommonCode.strings import Strings
from EntityModule.EntityQuery import EntityQuery
from EntityModule.EntityTableName import EntityTableName
from Environment.ServerListner import ServerListner
from PostgreSQLDatabase.PostgreSqlDataBaseConnection import PostgreSQLDatabaseConnection


class EntityQueryExecuter:
    m_helper = EntityQuery()
    m_dbConnection = PostgreSQLDatabaseConnection()
    m_encoder = IntigerToStringIdConverter()
    m_table = EntityTableName()
    m_serverEnvironment = ServerListner()
    id = None

    def get(self):
        try:
            query = self.m_helper.getEntityQuery(data=Strings.concatinateWithUnderScore(self.m_table.tableName(),
                                                                                        self.m_serverEnvironment.getServerEnvironment().name))
            print(query)
            conn = self.m_dbConnection.getConnection()
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchall()[0]
            self.id = row[1]
            conn.close()
            return self.m_encoder.convert(id=int(row[1]))
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

    def update(self):

        try:
            query = self.m_helper.updateEntityQuery(data=Strings.concatinateWithUnderScore(self.m_table.tableName(),
                                                                                           self.m_serverEnvironment.getServerEnvironment().name),
                                                    value=self.getIdNumber(self.id))
            print(query)
            conn = self.m_dbConnection.getConnection()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            count = cursor.rowcount
            conn.close()
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

    def getIdNumber(self, id):
        m_id = int(id)
        m_id = m_id + 1
        return str(m_id)

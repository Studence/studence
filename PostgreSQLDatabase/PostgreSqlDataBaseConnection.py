import psycopg2


connection = None

class PostgreSQLDatabaseConnection:

    DATABASE_NAME = "studence_db";
    USERNAME_NAME = "postgres";
    HOST= "127.0.0.1";
    PORT="5432";
    PASSWORD = "nikerisk";

    def getConnection(self):
        try:
            print("Your are Connecting...")
            global connection
            connection = psycopg2.connect(user=self.USERNAME_NAME,
                                          password=self.PASSWORD,
                                          host=self.HOST,
                                          port=self.PORT,
                                          database=self.DATABASE_NAME)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        if (connection):
            print("Your are Connected...")
        return connection

    def closeConnection(self, connection):
        connection.close()

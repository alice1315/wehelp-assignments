import mysql.connector
import mysql.connector.pooling

class Database:
    def __init__(self, config):
        self.config = config
        self.cnxpool = self.create_cnxpool()
        self.cnx = self.get_connection()

    def create_cnxpool(self):
        try:
            cnxpool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name = "cnxpool",
                pool_size = 2,
                **self.config
            )
        except mysql.connector.Error as err:
            print(err)
        
        return cnxpool
    
    def get_connection(self):
        cnx = self.cnxpool.get_connection()
        return cnx

    def execute_sql(self, sql, sql_data):
        try:
            cursor = self.cnx.cursor(dictionary=True)
            cursor.execute(sql, sql_data)
            result = cursor.fetchone()
        except:
            self.cnx.rollback()
        finally:
            cursor.close()
        
        return result

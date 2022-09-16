import mysql.connector

class Database:
    def __init__(self,host, user, passwd, database = ''):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
    
    def connect(self):
        self.db = mysql.connector.connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            database = self.database)
        self.cursor = self.db.cursor()
    
    def create_database(self,database_name):
        sql_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
        self.cursor.execute(sql_query)
        self.db.commit()
   
    def create_table(self,table_name,variables):
        sql_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({variables})"
        self.cursor.execute(sql_query)
        self.db.commit()
       
    def close_connection(self):
        self.db.close()
     
class Insert(Database):
    def __init__(self, host, user, passwd, database = ''):
        super().__init__(host, user, passwd, database)
        
    def insert_into_client(self, ):
        pass
    
    def insert_into_product(self, ):
        pass
    
    def insert_into_orders(self, ):
        pass
        
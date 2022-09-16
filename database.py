import mysql.connector

class Database:
    def __init__(self,host, user, passwd, database = ''):
        self.db = mysql.connector.connect(
            host = host,
            user = user,
            passwd = passwd,
            database = database)
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
     

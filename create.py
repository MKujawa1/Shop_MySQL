from database import Database

# Connection params
host = 'localhost'
user = 'Maciej'
passwd = 'password'
# Database param
database = 'Shop'
# Tables params
client_table_name = 'client'
client_table_variables = 'Id int PRIMARY KEY NOT NULL AUTO_INCREMENT,\
name VARCHAR(50) NOT NULL,\
surname VARCHAR(50) NOT NULL,\
email VARCHAR(50) NOT NULL,\
city VARCHAR(50) NOT NULL'
product_table_name = 'product'
product_table_variables = 'Id int PRIMARY KEY NOT NULL AUTO_INCREMENT,\
name VARCHAR(50) NOT NULL,\
price FLOAT NOT NULL'
order_table_name = 'orders'
order_table_variables = 'Id int PRIMARY KEY NOT NULL AUTO_INCREMENT,\
clientId int NOT NULL, FOREIGN KEY(clientId) REFERENCES client(Id),\
productId int NOT NULL, FOREIGN KEY(productId) REFERENCES product(Id),\
date datetime NOT NULL,\
status VARCHAR(50)'
 
db = Database(host=host,user=user,passwd = passwd)
db.connect()
db.create_database(database)
db.cursor.execute("SHOW DATABASES")
db.cursor.fetchall()
db = Database(host=host,user=user,passwd = passwd,database = database)
db.connect()
db.create_table(client_table_name,client_table_variables)
db.create_table(product_table_name,product_table_variables)
db.create_table(order_table_name,order_table_variables)
db.cursor.execute("SHOW TABLES")
db.cursor.fetchall()
db.cursor.execute("SHOW COLUMNS FROM orders")
db.cursor.fetchall()
db.close_connection()

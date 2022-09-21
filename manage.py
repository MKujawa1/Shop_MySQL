from database import Insert
from datetime import datetime

# Connection params
host = 'localhost'
user = 'Maciej'
passwd = 'password'
# Database param
database = 'Shop'
# Connecting
db = Insert(host=host,user=user,passwd = passwd,database = database)
db.connect()
# Adding records to tables
db.insert_into_client('Tomek','Charmek','charmek@gmail.com','Warszawa')
db.insert_into_client('Maciej','Paliot','m.p@o2.pl','Szczecin')
db.insert_into_client('Paulina','Grabowska','grab.paulina@gmail.com','Sopot')
db.insert_into_client('Kasia','Zaborska','kasia156k@gmail.com','Warszawa')
db.insert_into_client('Kacper','Wakowski','wakowski.kacper@o2.pl','Bydgoszcz')

db.insert_into_product('Koszulka', 59.99)
db.insert_into_product('Bluza', 99.99)
db.insert_into_product('Spodnie', 129.99)
db.insert_into_product('Buty', 259.99)
db.insert_into_product('Koszula', 109.99)

db.cursor.execute("SELECT id FROM client WHERE name = 'Tomek' AND surname = 'Charmek'")
clientId = db.cursor.fetchall()[0][0]
db.cursor.execute("SELECT id FROM product WHERE name = 'Koszulka'")
productId = db.cursor.fetchall()[0][0]
db.insert_into_orders(clientId, productId, datetime.now(), 'Oczekuje')

db.cursor.execute("SELECT id FROM client WHERE name = 'Paulina' AND surname = 'Grabowska'")
clientId = db.cursor.fetchall()[0][0]
db.cursor.execute("SELECT id FROM product WHERE name = 'Buty'")
productId = db.cursor.fetchall()[0][0]
db.insert_into_orders(clientId, productId, datetime.now(), 'Dostarczone')

db.cursor.execute("SELECT id FROM client WHERE name = 'Paulina' AND surname = 'Grabowska'")
clientId = db.cursor.fetchall()[0][0]
db.cursor.execute("SELECT id FROM product WHERE name = 'Koszulka'")
productId = db.cursor.fetchall()[0][0]
db.insert_into_orders(clientId, productId, datetime.now(), 'Dostarczone')

db.cursor.execute("SELECT id FROM client WHERE name = 'Kacper' AND surname = 'Wakowski'")
clientId = db.cursor.fetchall()[0][0]
db.cursor.execute("SELECT id FROM product WHERE name = 'Buty'")
productId = db.cursor.fetchall()[0][0]
db.insert_into_orders(clientId, productId, datetime.now(), 'Dostarczone')

db.cursor.execute("SELECT id FROM client WHERE name = 'Maciej' AND surname = 'Paliot'")
clientId = db.cursor.fetchall()[0][0]
db.cursor.execute("SELECT id FROM product WHERE name = 'Koszula'")
productId = db.cursor.fetchall()[0][0]
db.insert_into_orders(clientId, productId, datetime.now(), 'Oczekuje')

db.cursor.execute("SELECT id FROM client WHERE name = 'Tomek' AND surname = 'Charmek'")
clientId = db.cursor.fetchall()[0][0]
db.cursor.execute("SELECT id FROM product WHERE name = 'Bluza'")
productId = db.cursor.fetchall()[0][0]
db.insert_into_orders(clientId, productId, datetime.now(), 'Oczekuje')
# Read values from tables
db.cursor.execute('SELECT * FROM client')
db.cursor.fetchall()
db.cursor.execute('SELECT * FROM product')
db.cursor.fetchall()
db.cursor.execute('SELECT * FROM orders')
db.cursor.fetchall()
# Do some select operations
# Count and group status
db.cursor.execute('SELECT status, COUNT(status) FROM orders GROUP BY status ORDER BY COUNT(status) DESC')
for x in db.cursor:
    print(x)
# Get client name and surname, product name and status where is 'Oczekuje'
db.cursor.execute('SELECT c.name, c.surname, p.name, o.status \
                  FROM client AS c, product AS p, orders AS o WHERE \
                  o.status = "Oczekuje" AND o.clientId = c.Id AND o.productId = p.Id \
                  ORDER BY c.name' )
for x in db.cursor:
    print(x)
# Get name and surname of client with highest total order price
db.cursor.execute('SELECT c.name, c.surname, ROUND(SUM(p.price),2) \
                  FROM client AS c, product AS p, orders AS o WHERE \
                  o.clientId = c.Id AND o.productId = p.Id \
                  GROUP BY  o.clientID \
                  ORDER BY SUM(p.price) DESC, c.name ASC LIMIT 1')
for x in db.cursor:
    print(x)
# Close connection
db.close_connection()

from database import Insert

# Connection params
host = 'localhost'
user = 'Maciej'
passwd = 'password'
# Database param
database = 'Shop'

db = Insert(host=host,user=user,passwd = passwd,database = database)
db.connect()


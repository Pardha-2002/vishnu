import mysql.connector
myDB=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Pardha@2002'
)
print(myDB)
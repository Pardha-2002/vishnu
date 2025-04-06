import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "Pardha@2002",
)

print(myDB)

cursor = myDB.cursor()

cursor.execute("select * from revature.student")
for row in cursor:
    print(row)
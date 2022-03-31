import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ree2020',
    database='testdatabase'
)

cur = db.cursor()

cur.execute("INSERT INTO Person (name,age) VALUES(%s,%s)",('Erick',21))

db.commit()

cur.execute("SELECT * FROM Person")

for x in cur:
    print(x)

print("Success")
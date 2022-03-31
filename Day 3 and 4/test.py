import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ree2020",
    database="boatsdb",
    port = 3306
)
print("Hey, i think i'm connected")
#Cursor
cur = mydb.cursor()
#Execute the query
cur.execute("SELECT ID,NAME FROM boats where name = %s", ("Nathan",))

rows = cur.fetchall()

for r in rows:
    print(f" ID ={r[0]} NAME = {r[1]} ")

#Close the cursor
cur.close()
#Close the connection
mydb.close()
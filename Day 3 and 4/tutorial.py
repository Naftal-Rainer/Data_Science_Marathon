import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Ree2021',
    database = 'projects'    
)

mycursor = db.cursor()

names = ['Erick', 'Paul', 'Hajji', 'Mzazi']
ages = [20,21,19,25]


# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
# mycursor.execute("DESCRIBE Person")

# for x in mycursor:
#     print(x)



mycursor.execute("INSERT INTO Person (name , age ) VALUES(%s, %s)",("Stephen", 22))
db.commit()

mycursor.execute("SELECT * FROM Person")

for x in mycursor:
    print(x)

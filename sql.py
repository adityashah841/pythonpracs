# import mysql.connector
# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# password="Moonshine@123",
# )
# print(mydb)

# import mysql.connector
# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# password="Moonshine@123",
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE Electronics")

# import mysql.connector
# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# password="Moonshine@123",
# )
# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Moonshine@123",
#   database="electronics"
# )

# import mysql.connector
# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# password="Moonshine@123",
# database="electronics"
# )
# mycursor = mydb.cursor()
# mycursor.execute("""CREATE TABLE Laptop (Id int(11) NOT NULL, Name varchar(250) NOT NULL,Price float NOT NULL,Purchase_date Date NOT NULL,PRIMARY KEY (Id))""")

# import mysql.connector
# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# password="Moonshine@123",
# database="electronics"
# )
# mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#  print(x)

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Moonshine@123",
#   database="electronics"
# )
# mycursor = mydb.cursor()
# mycursor.execute("""INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
#                            VALUES 
#                            (15, 'Lenovo ThinkPad P71', 6459, '2019-08-14') """)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

#from msilib import Table
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Moonshine@123",
#   database="electronics"
# )
# mycursor = mydb.cursor()

# sql = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
#                            VALUES 
#                            (%s,%s,%s,%s) """
# val = [(2, 'Area 51M', 6999, '2019-04-14'),(3, 'MacBook Pro', 2499, '2019-06-20'),
#           (4, 'Asus', 8000, '2020-04-14'),(5, 'HP', 15000, '2019-05-10')]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Moonshine@123",
#   database="electronics"
# )
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM Laptop")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Moonshine@123",
#   database="electronics"
# )
# mycursor = mydb.cursor()
# mycursor.execute("SELECT ID, Name, Price FROM Laptop")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Moonshine@123",
#   database="electronics"
# )
# mycursor = mydb.cursor()
# mycursor.execute("SELECT ID, Name, Price FROM Laptop")
# myresult = mycursor.fetchone()
# for x in myresult:
#   print(x)

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Moonshine@123",
#   database="electronics"
# )
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM Laptop WHERE Name ='HP' ")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Moonshine@123",
#   database="electronics"
# )
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM Laptop WHERE Name LIKE 'A%' ")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Moonshine@123",
#   database="electronics"
# )
# mycursor = mydb.cursor()
# mycursor.execute("DELETE FROM Laptop WHERE NAME = 'Asus' ")
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Moonshine@123",
#   database="electronics"
# )
# mycursor = mydb.cursor()
# mycursor.execute("UPDATE Laptop SET Price = 15000 WHERE NAME = 'HP' ")
# mydb.commit()
# print(mycursor.rowcount, "record(s) updated")

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Moonshine@123",
#   database="electronics"
# )
# mycursor = mydb.cursor()
# mycursor.execute("ALTER TABLE Laptop ADD Year int(10) ")
# mydb.commit()

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Moonshine@123",
#   database="electronics"
# )
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM Laptop")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Moonshine@123",
  database="electronics"
)
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE Laptop")
mydb.commit()

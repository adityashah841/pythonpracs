import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "Moonshine@123",
    database = "bsdk"
)
cursor = myDB.cursor()
cursor.execute("""CREATE TABLE marks (id int(11),name varchar(50) NOT NULL, total_marks int(3), PRIMARY KEY (id) )""")

cursor.execute(""" INSERT INTO marks(id,name,total_marks) VALUES (1,"roy",82)""")
cursor.execute(""" INSERT INTO marks(id,name,total_marks) VALUES (2,"loy",89)""")
myDB.commit()

cursor.execute(""" DELETE from marks WHERE id=2 """)
myDB.commit()

cursor.execute(""" SELECT * FROM marks """)
for x in cursor:
    print(x)

cursor.execute(""" UPDATE marks SET total_marks = 50 WHERE id=1 """)
myDB.commit()

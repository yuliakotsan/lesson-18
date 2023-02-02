import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='jimmy',
    password='aq123esw',
    database='my_first_db'
)

mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE students ADD PRIMARY KEY(id)")
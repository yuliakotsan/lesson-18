import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='jimmy',
    password='aq123esw',
    database='my_first_db'
)

my_cursor = mydb.cursor()

sql = "INSERT INTO students (id, name) VALUES (%s, %s)"
val = (1, "John")
my_cursor.execute(sql, val)

sql = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
val = (1, "John", 10000)
my_cursor.execute(sql, val)

mydb.commit()
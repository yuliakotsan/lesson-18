import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='jimmy',
    password='aq123esw'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE my_first_db")




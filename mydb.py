import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
)

# prepare a cursor object
mycursor = database.cursor()

# create a data base
mycursor.execute("create database webco")

print("done")
import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = "root",
    passwd = "20033011"
)

# prepare cursor
cursorObj = dataBase.cursor()

# create a database
cursorObj.execute("CREATE DATABASE rewire")

print("databse created!")

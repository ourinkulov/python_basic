import mysql.connector

mydb = mysql.connector.connect(
    host = "172.16.2.4",
    user = "db_smart_reyting_user",
    passwd = "TahdeR963#2022@",
    database = "pytestdb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM pytest")
myresult = mycursor.fetchall()
for row in myresult:
     print(row)


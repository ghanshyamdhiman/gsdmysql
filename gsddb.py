#https://dev.mysql.com/doc/mysql-installation-excerpt/5.6/en/docker-mysql-getting-started.html
import mysql.connector

rm_host = 'localhost'
#rm_host = '192.168.0.25:3306'

mydb = mysql.connector.connect(
  host=rm_host,
  user="root",
  password="Gsd@12345",
  database="testdb1"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM testtbl1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

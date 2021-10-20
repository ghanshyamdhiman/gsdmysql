#https://dev.mysql.com/doc/mysql-installation-excerpt/5.6/en/docker-mysql-getting-started.html
#https://bobcares.com/blog/edit-docker-image/
#https://www.macstadium.com/blog/how-to-k8s-pull-edit-and-push-a-docker-image
#docker run -p 5432:5432 -it postgres
#https://www.sqlshack.com/how-to-connect-to-remote-mysql-server-using-ssl-on-ubuntu-18-04/
#SELECT host, user FROM mysql.user;

#GRANT ALL ON *.* TO 'myuser'@'localhost';
#GRANT ALL ON *.* TO 'myuser'@'%';
import mysql.connector

mydb = mysql.connector.connect(
  host='mysql',
  user="root",
  password="secret",
  database="todos"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE testtbl1(user_id VARCHAR(4), product_code VARCHAR(25))")
mycursor.execute("INSERT INTO testtbl1 values('u-01', 'pc-001')")
mycursor.execute("INSERT INTO testtbl1 values('u-02', 'pc-002')")
mycursor.execute("INSERT INTO testtbl1 values('u-03', 'pc-003')")
mycursor.execute("INSERT INTO testtbl1 values('u-04', 'pc-004')")


mycursor.execute("SELECT * FROM testtbl1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

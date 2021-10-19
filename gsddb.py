#https://dev.mysql.com/doc/mysql-installation-excerpt/5.6/en/docker-mysql-getting-started.html
#https://bobcares.com/blog/edit-docker-image/
#https://www.macstadium.com/blog/how-to-k8s-pull-edit-and-push-a-docker-image
#docker run -p 5432:5432 -it postgres
#https://www.sqlshack.com/how-to-connect-to-remote-mysql-server-using-ssl-on-ubuntu-18-04/
#SELECT host, user FROM mysql.user;

#GRANT ALL ON *.* TO 'myuser'@'localhost';
#GRANT ALL ON *.* TO 'myuser'@'%';
import mysql.connector

#rm_host = '0.0.0.0'
rm_host = '172.17.0.1'

mydb = mysql.connector.connect(
  host=rm_host,
  user="gsd",
  password="gsd123",
  database="testdb1"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM testtbl1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

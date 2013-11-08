#mysql-buildsamples
import MySQLdb

db = MySQLdb.connect("127.0.0.1","shippable","")
cursor = db.cursor()
cursor.execute("DROP DATABASE IF EXISTS TESTDB")

cursor.execute("CREATE DATABASE TESTDB")

cursor.execute("USE TESTDB")

#creating TABLE
sql1 = """CREATE TABLE EMPLOYEE (
         NAME  CHAR(20) NOT NULL,
         AGE INT
         INCOME FLOAT )"""
cursor.execute(sql1)

#inserting VALUES
sql2 = """INSERT INTO EMPLOYEE(NAME,
         AGE, INCOME)
         VALUES ('Mohan', 20, 5000)"""
try:
   cursor.execute(sql2)
   db.commit()
except:
   db.rollback()


# Query
sql3 = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
   cursor.execute(sql3)
   results = cursor.fetchall()
   for row in results:
      name = row[0]
      age = row[1]
      income = row[2]
      print "name=%s,age=%d,income=%d" % \
             (name, age, income )
except:
   print "Error: unable to fecth data"
   
db.close()

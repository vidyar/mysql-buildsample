#mySql build sample
import MySQLdb

db = MySQLdb.connect("127.0.0.1","shippable")
cursor = db.cursor()
cursor.execute("DROP DATABASE IF EXISTS TESTDB")

cursor.execute("CREATE DATABASE TEST-DB")

cursor.execute("USE TEST-DB")

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#creating TABLE
sql1 = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql1)

#inserting VALUES
sql2 = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
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
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )
except:
   print "Error: unable to fecth data"
   
db.close()

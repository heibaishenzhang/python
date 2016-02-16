
#Connect to MySQL database
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

DB_URL='localhost'
USER_NAME='root'
PASSWD='1234'
DB_NAME='test'

# �����ݿ�����
db = MySQLdb.connect(DB_URL,USER_NAME,PASSWD,DB_NAME)

# ʹ��cursor()������ȡ�����α� 
cursor = db.cursor()

# ʹ��execute����ִ��SQL���
cursor.execute("SELECT VERSION()")

# ʹ�� fetchone() ������ȡһ�����ݿ⡣
data = cursor.fetchone()

print "Database version : %s " % data

# �ر����ݿ�����
db.close()



#Create tables
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# �����ݿ�����
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# ʹ��cursor()������ȡ�����α� 
cursor = db.cursor()

# ������ݱ��Ѿ�����ʹ�� execute() ����ɾ����
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# �������ݱ�SQL���
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# �ر����ݿ�����
db.close()


#Insert record into database
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# �����ݿ�����
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# ʹ��cursor()������ȡ�����α� 
cursor = db.cursor()

# SQL �������
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # ִ��sql���
   cursor.execute(sql)
   # �ύ�����ݿ�ִ��
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# �ر����ݿ�����
db.close()

#query the tables
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# �����ݿ�����
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# ʹ��cursor()������ȡ�����α� 
cursor = db.cursor()

# SQL ��ѯ���
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
   # ִ��SQL���
   cursor.execute(sql)
   # ��ȡ���м�¼�б�
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # ��ӡ���
      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )
except:
   print "Error: unable to fecth data"

# �ر����ݿ�����
db.close()



#Update the record
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# �����ݿ�����
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# ʹ��cursor()������ȡ�����α� 
cursor = db.cursor()

# SQL �������
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1
                          WHERE SEX = '%c'" % ('M')
try:
   # ִ��SQL���
   cursor.execute(sql)
   # �ύ�����ݿ�ִ��
   db.commit()
except:
   # ��������ʱ�ع�
   db.rollback()

# �ر����ݿ�����
db.close()



import mysql.connector as conn
#SQL=Structured Query Language

mydb=conn.connect(host="localhost",user="root",passwd="Rockandroll77")
cursor=mydb.cursor()
# cursor.execute("show databases")
# print(cursor.fetchall())

#Creating New Databases
# cursor.execute("create database jigglejiggle")
# cursor.execute("show databases")
# print(cursor.fetchall())

# q1=cursor.execute("create table jigglejiggle.details(employee_id int(10),employee_name varchar(80), employee_mailid varchar(100),employee_salary int(6),employee_attendance int(3))")

q2=cursor.execute("select * from jigglejiggle.details")
print(q2)




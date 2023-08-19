import pymysql

# 1. create a connection
con=pymysql.connect(host='localhost',user='root',db='mpvit')
print("Connection mil gaya")
mycursor=con.cursor()
'''
sql="create table student_info(name varchar(35), age int(2))"
mycursor.execute(sql)
print("table created successfully")
'''

name1='mohan'
age1=40
sqlins="insert into student_info(name,age)values(%s,%s)"
val=(name1,age1)
mycursor.execute(sqlins,val)
'''
sqlup="update student_info set age=434 where name='abcd'"
mycursor.execute(sqlup)
'''
con.commit() # to store data permanently
print("data updated successfully")
# last step. close connection
con.close()
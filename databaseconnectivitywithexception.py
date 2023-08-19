import pymysql
conn=''
try:
    conn = pymysql.connect(host="localhost", user="root", db="mpvit")
    mycursor = conn.cursor()
    sql_select_Query = "select * from student_info "

    mycursor.execute(sql_select_Query)

    records = mycursor.fetchall()
    print(records)

    print("Total number of rows in student_info is - ", mycursor.rowcount)


    for row in records:
        print("Name = ", row[0] )
        print("age = ", row[1],"\n")



except ValueError as e:
    print("Error while connecting to MySQL", e)
finally:
   conn.close()
   print("MySQL connection is closed")
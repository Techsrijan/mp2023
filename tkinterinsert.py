from tkinter import *
import pymysql
root=Tk()
def db_connect():
    global mycursor,con
    con = pymysql.connect(host='localhost', user='root', db='mpvit')
    mycursor = con.cursor()

def gettext():
   name1=a.get()
   age1=b.get()
   print(name1,age1)
   db_connect()
   sqlins = "insert into student_info(name,age)values(%s,%s)"
   val = (name1, age1)
   mycursor.execute(sqlins, val)
   con.commit()  # to store data permanently
   print("data inserted" )
   a.set('')
   b.set('')

btn4=Button(root,text="Save Data",bg="black",fg="yellow",
        font=("Comic Sans Ms",15,"bold"),command=gettext)
btn4.place(x=50,y=150)

a=StringVar()
txt=Entry(root,font=("Comic Sans Ms",15,"bold"),textvariable=a)
txt.place(x=200,y=150)

b=IntVar()
l=Entry(root,font=("Comic Sans Ms",15,"bold"),textvariable=b)
l.place(x=200,y=220)
root.geometry("600x300+180+250")
root.mainloop()
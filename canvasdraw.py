from tkinter import *

root=Tk()
c=Canvas(root,height=500,width=600,bg="white")
b=c.create_line(0,0,300,200,fill='red',width=20)
# d=c.create_rectangle(50,80,200,300,fill="green")
# c1=c.create_oval(50,80,200,300,fill="yellow")

s=c.create_rectangle(0,0,200,200,fill="green")
s1=c.create_oval(0,0,200,200,fill="blue")
c.pack()
root.mainloop()
from tkinter import *
def gettext():
    c=int(a.get())
    d = int(b.get())
    #print(c+d)
    result.set(c+d)
root=Tk()
l=Label(root,text="Enter first Number",
        font=("Comic Sans Ms",15,"bold"))
l.grid(row=0,column=0)

a=StringVar()
txt=Entry(root,bd="10",justify="right",font=("Comic Sans Ms",15,"bold"),textvariable=a)
txt.grid(row=0,column=1)


l2=Label(root,text="Enter Second Number",
        font=("Comic Sans Ms",15,"bold"))
l2.grid(row=1,column=0)
b=StringVar()
txt2=Entry(root,bd="10",justify="right",font=("Comic Sans Ms",15,"bold"),textvariable=b)
txt2.grid(row=1,column=1)

btn4=Button(root,text="Add",bg="black",fg="yellow",
        font=("Comic Sans Ms",15,"bold"),command=gettext)
btn4.grid(row=2,column=0,columnspan=2)

result=StringVar()
l3=Label(root,
        font=("Comic Sans Ms",15,"bold"),textvariable=result)
l3.grid(row=3,column=0,columnspan=2)
root.mainloop()
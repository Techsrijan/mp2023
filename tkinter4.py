from tkinter import *
root=Tk()
def gettext():
    c=a.get()
    #print(c)
    result.set(c)

btn4=Button(root,text="click me4",bg="black",fg="yellow",
        font=("Comic Sans Ms",15,"bold"),command=gettext)
btn4.place(x=50,y=150)

a=IntVar()
txt=Entry(root,font=("Comic Sans Ms",15,"bold"),textvariable=a)
txt.place(x=200,y=150)

result=StringVar()
# l=Label(root,
#         font=("Comic Sans Ms",15,"bold"),textvariable=result)
# l.place(x=200,y=220)


l=Entry(root,
        font=("Comic Sans Ms",15,"bold"),textvariable=result)
l.place(x=200,y=220)
root.geometry("600x300+180+250")
root.mainloop()
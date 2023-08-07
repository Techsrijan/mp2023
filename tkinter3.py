from tkinter import *
root=Tk()
btn4=Button(root,text="click me4",bg="black",fg="yellow",
        font=("Comic Sans Ms",15,"bold"))
btn4.place(x=50,y=150)

l=Label(root,text="This is my first Label",bg="red",fg="yellow",
        font=("Comic Sans Ms",15,"bold"))
l.place(x=200,y=150)
root.geometry("600x300+180+250")
root.mainloop()
from tkinter import *
root=Tk()

def greet():
    print("Good morning")

def greet2():
    print("Good evening")

root.title("My Calculator")
l=Label(root,text="This is my first Label",bg="red",fg="yellow",
        font=("Comic Sans Ms",15,"bold"))
l.pack()
btn=Button(root,text="click me",bg="black",fg="yellow",
        font=("Comic Sans Ms",15,"bold"),command=greet)
btn.pack()

btn2=Button(root,text="click me2",bg="black",fg="yellow",
        font=("Comic Sans Ms",15,"bold"),command=greet2)
btn2.pack()
root.resizable(0,0)
root.geometry("500x400+350+400")
root.mainloop()
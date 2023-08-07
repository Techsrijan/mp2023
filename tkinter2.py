from tkinter import *
root=Tk()


btn1=Button(root,text="click me1",bg="black",fg="yellow",
        font=("Comic Sans Ms",15,"bold"))
btn1.pack(side='top',fill='x')

btn2=Button(root,text="click me2",bg="black",fg="yellow",
        font=("Comic Sans Ms",15,"bold"))
btn2.pack(side="bottom")

btn3=Button(root,text="click me3",bg="black",fg="yellow",
        font=("Comic Sans Ms",15,"bold"))
btn3.pack(side="left",fill="y")

btn4=Button(root,text="click me4",bg="black",fg="yellow",
        font=("Comic Sans Ms",15,"bold"))
btn4.pack(side="right")
root.geometry("400x300+180+250")
root.mainloop()
from tkinter import *
root=Tk()
def rightClick(event):
    print("rightClick is pressed")
def leftClick(event):
    print("leftClick is pressed")
def scrollClick(event):
    print("scrollClick is pressed")
btn4=Button(root,text="right",bg="black",fg="yellow",
        font=("Comic Sans Ms",15,"bold"))
btn4.bind("<Button-1>",rightClick)
btn4.pack()

btn5=Button(root,text="left",bg="black",fg="yellow",
        font=("Comic Sans Ms",15,"bold"))
btn5.bind("<Button-3>",leftClick)
btn5.pack()

btn6=Button(root,text="scroll",bg="black",fg="yellow",
        font=("Comic Sans Ms",15,"bold"))
btn6.bind("<Button-2>",scrollClick)
btn6.pack()
root.mainloop()
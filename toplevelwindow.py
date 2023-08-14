from tkinter import *
def test():
    print("Good")
def openwindow():
    top=Toplevel(root)
    btn4 = Button(top, text="close", command=top.destroy)
    btn4.pack()

    btn5 = Button(top, text="test", command=test)
    btn5.pack()
    top.geometry("400x500+120+120")
root=Tk()
btn=Button(root,text="open window",command=openwindow)
btn.pack()
btn1=Button(root,text="close",command=quit)
btn1.pack()
root.geometry("400x500+120+120")


root.mainloop()
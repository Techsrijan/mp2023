from tkinter import *
from tkinter import simpledialog
def getdata():
    for i in range(4):
        s=simpledialog.askinteger(title="Marks Input Window",prompt='Please Enter The Marks')
        print(s)
root=Tk()
btn=Button(root,text="Input Marks",command=getdata)
btn.pack()
btn1=Button(root,text="close",command=quit)
btn1.pack()
root.geometry("400x500+120+120")


root.mainloop()
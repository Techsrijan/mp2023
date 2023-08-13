from tkinter import *
def getdata():
    print(s.get())
    print(sp.get())
root=Tk()
s=Scale(root,from_=10000, to=200000,orient=HORIZONTAL,length=400,width=50,sliderlength=150)
s.set(50)
s.pack()

sp=Spinbox(root,from_=1,to=5)
sp.pack()
btn=Button(root,text="click to get value",command=getdata).pack()
root.geometry("400x600+120+120")
root.mainloop()
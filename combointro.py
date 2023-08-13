from tkinter import *
from tkinter import ttk
def getdata():
   print(a.get())
root=Tk()
l=["C","Java","Python"]
a=StringVar()
combo=ttk.Combobox(root,value=l,textvariable=a)
combo.set("Select any Language")
combo.pack()
btn=Button(root,text="click to get value",command=getdata).pack()
root.geometry("400x600+120+120")
root.mainloop()

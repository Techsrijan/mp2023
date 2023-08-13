from tkinter import *

def getdata():
    item=l.curselection()
    print(item)
    for x in item:
        print(l.get(x))

def deldata():
    item = l.curselection()
    print(item)
    for x in item:
        print(l.delete((item)))

def insertdata():
    d=s.get()
    l.insert(END,d)
root=Tk()
f=Frame(root)
scroll=Scrollbar(f)

l=Listbox(f,height=15,width=15,selectmode=EXTENDED,
          yscrollcommand=scroll.set)
scroll.pack(fill=Y,side=RIGHT)
'''
l.insert(END,"Rohan")
l.insert(END,"Mohan")'''
s=StringVar()
text=Entry(root,textvariable=s)
text.pack()
for i in range(20):
    l.insert(END,"Happy B-days="+str(i))
scroll.config(command=l.yview)
l.pack(side=LEFT)
f.pack()

btnins=Button(root,text="click to insert",command=insertdata).pack()
btn=Button(root,text="click to get value",command=getdata).pack()

btndelete=Button(root,text="click to delete value",command=deldata).pack()
root.geometry("400x600+120+120")
root.mainloop()

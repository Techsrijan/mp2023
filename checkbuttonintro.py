from tkinter import *
def getData():
    print(j.get())
    print(k.get())

root=Tk()


Lblframe=LabelFrame(root,text="       Select Known Language           ")
j=IntVar()
k=StringVar()
l=IntVar()
c1=Checkbutton(Lblframe,text="Hindi",variable=j,offvalue=0,onvalue=1)
c1.pack()
c2=Checkbutton(Lblframe,text="English",variable=k)
c2.pack()
c3=Checkbutton(Lblframe,text="Urdu",variable=l)
c3.pack()
Lblframe.pack()
btn=Button(root,text="Get Radio data",command=getData)
btn.pack()
root.mainloop()
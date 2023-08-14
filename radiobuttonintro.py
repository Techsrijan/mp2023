from tkinter import *
def getData():
    print(i.get())
    if i.get()==1:
        print("Male")
    else:
        print("Female")
root=Tk()
i=IntVar()
r1=Radiobutton(root,text="Male",value=1,variable=i)
r1.pack()
r2=Radiobutton(root,text="FeMale",value=2,variable=i)
r2.pack()

Lblframe=LabelFrame(root,text="       Select Type of School           ")
j=IntVar()
r3=Radiobutton(Lblframe,text="Govt",value=1,variable=j)
r3.pack()
r4=Radiobutton(Lblframe,text="Private",value=2,variable=j)
r4.pack()
Lblframe.pack()
btn=Button(root,text="Get Radio data",command=getData)
btn.pack()
root.mainloop()
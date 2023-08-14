from tkinter import *
from tkinter import filedialog
def getdata():
    print(txt.get(1.0,END))
def selecteddata():
    result=txt.selection_get()
    print(result)
def cleardata():
    txt.delete(1.0, END)
def posdata():
    result = txt.selection_get()
    pos=txt.search(result,1.0,END)
    print(pos)
def openfile():
    res=filedialog.askopenfile(initialdir="/",title="Select file to open",
                               filetype=(("Text FILE","*.txt"),("All FILE","*.*")))
    print(res)
    for data in res:
        #print(data)
        txt.insert(INSERT, data)

root=Tk()
txt=Text(root,wrap=WORD, selectbackground='red')
#txt.pack(fill='both',expand=1)
#txt.insert(INSERT,'hello how are you')
txt.pack()
btn_openfile=Button(root,text="openfile",command=openfile)
btn_openfile.pack()
btn_pos=Button(root,text="select data position",command=posdata)
btn_pos.pack()
btn=Button(root,text="get data",command=getdata)
btn.pack()
btn3=Button(root,text="select data",command=selecteddata)
btn3.pack()
btn_clear=Button(root,text="Clear data",command=cleardata)
btn_clear.pack()
btn1=Button(root,text="close",command=quit)
btn1.pack()
root.geometry("400x500+120+120")


root.mainloop()
from tkinter import *

class MyWindow:
    def test(self):
        print("hi")

    def __init__(self,window):
        self.btn=Button(window,text="Click me",command=self.test)
        self.btn.pack()

        self.btn2 = Button(window, text="Exit", command=quit)
        self.btn2.pack()

root=Tk()
w=MyWindow(root)
root.mainloop()
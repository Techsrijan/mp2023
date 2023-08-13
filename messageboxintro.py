from tkinter import *
from tkinter import messagebox
root=Tk()
result=messagebox.askyesno(title="Confirmation Message",
                    message="Are u ready to go to college?")

#result=messagebox.showerror(title="Error Message")

if result==True:
    print("yes")
else:
    print("No")
print(result)
root.geometry("400x600+120+120")
root.mainloop()
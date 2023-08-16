from tkinter import *
def test():
    print("hi")
root=Tk()
main_menu=Menu(root)
root.config(menu=main_menu)
file_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",accelerator="Ctrl+n",command=test)
file_menu.add_command(label="Open",accelerator="Ctrl+o")

#edit_menu
edit_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",accelerator="Ctrl+x")
edit_menu.add_separator()
edit_menu.add_command(label="Copy",accelerator="Ctrl+c")
#root.wm_iconbitmap('calc.ico')
root.mainloop()
from tkinter import *
from tkinter import messagebox
import pymysql
taz=Tk()
h=taz.winfo_screenheight()
w=taz.winfo_screenwidth()
#print(h,w)
############### database connectivity #################
def db_connect():
    global mycursor,con
    con = pymysql.connect(host='localhost', user='root', db='tazhotel')
    mycursor = con.cursor()

#########################remove all widgets from screen #################

def remove_all_widgets():
    global taz
    for widget in taz.winfo_children():
        widget.grid_remove()

##############  main heading  ###################
def mainHeading():
    head = Label(taz, text="               TAZ HOTEL MANAGEMENT SYSTEM            ", bg='powderblue',
                 fg='black', font=("Comic Sans Ms", 25, 'bold'),
                 padx=20, pady=20)
    head.grid(row=0, column=0, columnspan=4)

################log out###############
def adminLogout():
    remove_all_widgets()
    adminLogin()
########### welcome window #########################
def welcomewindow():
    remove_all_widgets()
    mainHeading()
    windowLabel = Label(taz, text="Admin Window", font="Arial 20")
    windowLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)
    btnLogout = Button(taz, text="Logout", font="Arial 15", bg="green", fg="white", command=adminLogout)
    btnLogout.grid(row=2, column=1, padx=20, pady=5, columnspan=2)
############### adminLoginProcess ###################
def adminLoginProcess():
    if usernameVar.get()=='' or passwordVar.get()=='':
        messagebox.showerror(title="Login Error",message="Please Fill User Name and Password")
    else:
        db_connect()
        #print(usernameVar.get())
        #print(passwordVar.get())
        username = usernameVar.get().strip()
        password = passwordVar.get().strip()
        que = "select * from login_info where binary username=%s and binary password=%s"
        val = (username, password)
        mycursor.execute(que, val)
        data = mycursor.fetchall()
        flag = False
        for row in data:
            flag = True

        con.close()
        if flag == True:
            welcomewindow()

        else:
            messagebox.showerror(title="Login Error", message="Either USerName or Password is Incorrect")
            usernameVar.set('')
            passwordVar.set('')

############# Admin Login Window ###################
usernameVar = StringVar()
passwordVar = StringVar()
def adminLogin():
    mainHeading()
    loginLabel = Label(taz, text="Admin Login", font="Arial 20")
    loginLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    usernameLabel = Label(taz, text="Username",font="Arial 15")
    usernameLabel.grid(row=2, column=1, padx=20, pady=5)

    userNameEntry=Entry(taz,font="Arial 15",textvariable=usernameVar)
    userNameEntry.grid(row=2, column=2, padx=20, pady=5)

    passwordLabel = Label(taz, text="Password",font="Arial 15")
    passwordLabel.grid(row=3, column=1, padx=20, pady=5)

    passwordEntry = Entry(taz, font="Arial 15",show="*",textvariable=passwordVar)
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)

    btnLogin=Button(taz,text="Login",font="Arial 15",bg="green", fg="white",command=adminLoginProcess)
    btnLogin.grid(row=4, column=1, padx=20, pady=5 ,columnspan=2)


taz.title("Taz Hotel")
adminLogin()
taz.geometry("%dx%d+0+0"%(w,h))
taz.mainloop()
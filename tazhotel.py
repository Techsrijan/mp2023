from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
taz=Tk()
h=taz.winfo_screenheight()
w=taz.winfo_screenwidth()
#print(h,w)
# ========mainTreeView======================
tazTV = ttk.Treeview(height=10, columns=('Item Name''Rate','Type'))
############# validation ######################
def only_numeric_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False

def only_char_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isalpha() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False



callback = taz.register(only_char_input)  # registers a Tcl to Python callback
callback1 = taz.register(only_numeric_input)  # registers a Tcl to Python callback

############ billgenerationwindow ##########
def billgenerationwindow():
    pass

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

########### back button ########
def backbutton():
    remove_all_widgets()
    welcomewindow()

def OnDoubleClick(event):
    #print("hi")
    item = tazTV.selection()
    itemNameVar1 = tazTV.item(item, "text")
    item_detail = tazTV.item(item, "values")
    print(itemNameVar1,item_detail)
    itemnameVar.set(itemNameVar1)
    itemrateVar.set(item_detail[0])
    itemTypeVar.set(item_detail[1])
######### getIteminTreeView ###########
def getIteminTreeView():
    # to delete already inserted item
    records = tazTV.get_children()

    for element in records:
        tazTV.delete(element)

    # insert data in treeview
    conn = pymysql.connect(host="localhost", user="root", db="tazhotel")
    mycursor = conn.cursor(pymysql.cursors.DictCursor)
    query = "select * from itemlist"
    mycursor.execute(query)
    data = mycursor.fetchall()
    #print(data)
    for row in data:
        tazTV.insert('', 'end', text=row['item_name'], values=(row["item_rate"],
                                                               row["item_type"]))
    conn.close()
############################
def additem():
    item_name=itemnameVar.get()
    item_rate=itemrateVar.get()
    item_type=itemTypeVar.get()
    if item_name=='' or item_rate=='' or item_type=='':
        messagebox.showerror(title='Item Insert Error',
                             message='Please Fill all Details')
    else:
        db_connect()
        query = "insert into itemlist (item_name,item_rate,item_type) values(%s,%s,%s)"
        val = (item_name, item_rate, item_type)
        mycursor.execute(query, val)
        con.commit()
        messagebox.showinfo("Save Data", 'Item Inserted Successfully')
        itemnameVar.set("")
        itemrateVar.set("")
        itemTypeVar.set("")
        getIteminTreeView()
def updateItem():
    item_name = itemnameVar.get()
    item_rate = itemrateVar.get()
    item_type = itemTypeVar.get()
    if item_name == '' or item_rate == '' or item_type == '':
        messagebox.showerror(title='Item Insert Error',
                             message='Please Fill all Details')
    else:
        db_connect()
        query = "update itemlist set item_rate=%s, item_type=%s where item_name=%s"
        val = (item_rate, item_type,item_name)
        mycursor.execute(query, val)
        con.commit()
        messagebox.showinfo("Update Data", 'Item Updateded Successfully')
        itemnameVar.set("")
        itemrateVar.set("")
        itemTypeVar.set("")
        getIteminTreeView()
def deleteItem():
    item_name = itemnameVar.get()
    item_rate = itemrateVar.get()
    item_type = itemTypeVar.get()
    if item_name == '' or item_rate == '' or item_type == '':
        messagebox.showerror(title='Item Insert Error',
                             message='Please Fill all Details')
    else:
        db_connect()
        query = "delete from itemlist where item_name=%s "
        val = (item_name)
        mycursor.execute(query, val)
        con.commit()
        messagebox.showinfo("Delete Data", 'Item Deleted Successfully')
        itemnameVar.set("")
        itemrateVar.set("")
        itemTypeVar.set("")
        getIteminTreeView()





########## additemwindow #########

itemnameVar=StringVar()
itemrateVar=StringVar()
itemTypeVar=StringVar()
def additemwindow():
    remove_all_widgets()
    mainHeading()
    itemnameLabel = Label(taz, text="ITEM DETAILS", font="Arial 30")
    itemnameLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    ###############################
    billButton = Button(taz, text="Back", width=20, height=2, fg="green", bd=10, command=backbutton)
    billButton.grid(row=1, column=0)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=adminLogout)
    logoutButton.grid(row=1, column=3)

    ###########################

    itemnameLabel = Label(taz, text="Item name")
    itemnameLabel.grid(row=2, column=1, padx=20, pady=5)

    itemrateLabel = Label(taz, text="Item Rate")
    itemrateLabel.grid(row=3, column=1, padx=20, pady=5)

    itemTypeLabel = Label(taz, text="Item Type")
    itemTypeLabel.grid(row=4, column=1, padx=20, pady=5)

    itemnameEntry = Entry(taz, textvariable=itemnameVar)
    itemnameEntry.grid(row=2, column=2, padx=20, pady=5)
    itemnameEntry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation

    itemrateEntry = Entry(taz, textvariable=itemrateVar)
    itemrateEntry.grid(row=3, column=2, padx=20, pady=5)
    itemrateEntry.configure(validate="key", validatecommand=(callback1, "%P"))  # enables validation

    itemTypeEntry = Entry(taz, textvariable=itemTypeVar)
    itemTypeEntry.grid(row=4, column=2, padx=20, pady=5)
    itemTypeEntry.configure(validate="key", validatecommand=(callback, "%P"))  # enabl

    updateButton = Button(taz, text="UpDate Item", width=20, height=2, fg="green", bd=10, command=updateItem)
    updateButton.grid(row=6, column=0)

    additemButton = Button(taz, text="Add Item", width=20, height=2, fg="green", bd=10, command=additem)
    additemButton.grid(row=6, column=1,columnspan=2)


    deleteButton = Button(taz, text="Delete Item", width=20, height=2, fg="green", bd=10, command=deleteItem)
    deleteButton.grid(row=6, column=3)

    ################# to display treeview ##############################
    tazTV.grid(row=7, column=0, columnspan=4)
    scrollBar = Scrollbar(taz, orient="vertical", command=tazTV.yview)
    scrollBar.grid(row=7, column=4, sticky="NSE")

    tazTV.configure(yscrollcommand=scrollBar.set)

    tazTV.heading('#0', text="Item Name")
    tazTV.heading('#1', text="Rate")
    tazTV.heading('#2', text="Type")
    # get data in treeview
    getIteminTreeView()
    tazTV.bind("<Double-1>", OnDoubleClick)
########### welcome window #########################
def welcomewindow():
 remove_all_widgets()
 mainHeading()
 welcomeLabel = Label(taz, text="Welcome User", font="Arial 30")
 welcomeLabel.grid(row=1, column=0, padx=(50, 0), columnspan=3, pady=10)

 additemButton = Button(taz, text="Manage Restaurant", width=20, height=2, fg="green", bd=10, command=additemwindow)
 additemButton.grid(row=3, column=0)

 billButton = Button(taz, text="Bill Generation", width=20, height=2, fg="green", bd=10,
                     command=billgenerationwindow)
 billButton.grid(row=3, column=1)

 logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=adminLogout)
 logoutButton.grid(row=3, column=2)
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
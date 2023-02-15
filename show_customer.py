from tkinter import *
from tkinter import ttk
import sqlite3
root =Tk() 
root.title("Customer details")

style=ttk.Style()

style.theme_use('default')

style.configure("treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

style.map('Treeview',
    background=[('selected','#347083')])

try:
    sqliteconnection=sqlite3.connect("customer.db")
    cursor=sqliteconnection.cursor()
    print("Database created and successfully connected")

    sqlite_select_query="select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record=cursor.fetchall()
    print("sqlite Database version is :",record)
    cursor.close()

except sqlite3.Error as error:
    print("Error connecting to the sqlite",error)


tree_frame= Frame(root)
tree_frame.pack(pady=10)

tree_scroll= Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

my_tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="extended")
my_tree.pack()

tree_scroll.config(command=my_tree.yview)

#Defining columns
my_tree['columns']=("Full Name","Account Number","Deposit","Withdraw","Address","Email")

#Formating colums
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("Full Name",anchor=W,width=140)
my_tree.column("Account Number",anchor=W,width=140)
my_tree.column("Deposit",anchor=CENTER,width=140)
my_tree.column("Withdraw",anchor=CENTER,width=140)
my_tree.column("Address",anchor=CENTER,width=140)
my_tree.column("Email",anchor=CENTER,width=140)



#creating headings
my_tree.heading("#0",text="",anchor=W)
my_tree.heading("Full Name",text="Full Name",anchor=W)
my_tree.heading("Account Number",text="Account Number",anchor=W)
my_tree.heading("Deposit",text="Deposit",anchor=CENTER)
my_tree.heading("Withdraw",text="Withdraw",anchor=CENTER)
my_tree.heading("Address",text="Address",anchor=CENTER)
my_tree.heading("Email",text="Email",anchor=CENTER)

#creating tables

try:
    sqliteconnection=sqlite3.connect('banks.db')
    sqlite_create_table_query='''CREATE TABLE customers(
                               Full_name Text NOT NULL,
                               Account_num integer,
                               Deposit integer,
                               Withdraw integer,
                               Email varchar);'''
    cursor=sqliteconnection.cursor()
    print("Successfully connected to sqlite")
    cursor.execute(sqlite_create_table_query)
    sqliteconnection.commit()
    print("Sqlite table created")
    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table",error)


#insertimg values into table




#adding some data
# data=[

# ["Misheel Rai","34532631134","4000","","Damak","raimgmail.com"]

# ["Misheel Rai","34532631134","4000","","Damak","raimgmail.com"]

# ["Misheel Rai","34532631134","4000","","Damak","raimgmail.com"]

# ["Misheel Rai","34532631134","4000","","Damak","raimgmail.com"]
# ]



#creating striped row tags
my_tree.tag_configure("oddrow",background="White")
my_tree.tag_configure("evenrow",background="lightblue")

#adding data
# global count
# count=0
# for record in data:
#     if count %2 ==0:
#         my_tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]),tags='evenrow',)
 
#     else:
#         my_tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]),tags='oddrow',)

#     count+=1











# def show():

#     tempList = [['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5']]
#     tempList.sort(key=lambda e: e[1], reverse=True)

#     for i, (name, score) in enumerate(tempList, start=1):
#         listBox.insert("", "end", values=(i, name, score))

    
# label = tk.Label(root, text="Customer Details", font=("Arial",30)).grid(row=0, columnspan=3)
# # create Treeview with 3 columns
# cols = ('Full Name', 'Account Number', 'Deposit','Withdraw','Address','Gender','Email')
# listBox = ttk.Treeview(root, columns=cols, show='headings')
# # set column headings
# for col in cols:
#     listBox.heading(col, text=col)    
#     listBox.grid(row=1, column=0, columnspan=2)

# showScores = tk.Button(root, text="Show Details", width=15, command=show).grid(row=4, column=0)
# closeButton = tk.Button(root, text="Close", width=15, command=exit).grid(row=4, column=1)

root.mainloop()


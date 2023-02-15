from tkinter import *
from tkinter import messagebox
from time import strftime,gmtime
from PIL import ImageTk, Image
import sqlite3
root=Tk()
root.title("Withdraw money")
root["background"]="pink"

welcome=Label(root, text="Enter customer details to Withdraw ", font=("Verdana Bold", 12),bg="oldlace", fg="blue2")
welcome.grid(row=0,column=0)

frame2 = Frame(root,bg="white",height=300,width=800)
frame2.grid(row=1,column=3,rowspan=4,columnspan=4,pady=30,padx=40)

img = Image.open("withdraw.jpg")

bank_img = ImageTk.PhotoImage(img)
label_img = Label(frame2,image=bank_img).grid(row=0,column=0)

name=Entry(root,width=30)
name.grid(row=1,column=1)

account_num=Entry(root,width=30)
account_num.grid(row=2,column=1)

amount_to_withdraw=Entry(root,width=30)
amount_to_withdraw.grid(row=3,column=1)

name_label=Label(root,text="Name")
name_label.grid(row=1,column=0)

account_num_label=Label(root,text="Account Number")
account_num_label.grid(row=2,column=0)

amount_to_withdraw_label=Label(root,text="Amount to Withdraw")
amount_to_withdraw_label.grid(row=3,column=0)

Deposite_btn=Button(root,text="Withdraw", fg="white", bg="blue2",font=("Verdana Bold", 14))
Deposite_btn.grid(row=10,column=1)

# create a database connection and a cursor

try:
    sqliteconnection=sqlite3.connect("banks.db")
    cursor=sqliteconnection.cursor()
    print("Database created and successfully connected")

    sqlite_select_query="select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record=cursor.fetchall()
    print("sqlite Database version is :",record)
    cursor.close()

except sqlite3.Error as error:
    print("Error connecting to the sqlite",error)

#create table
try:
    sqliteconnection=sqlite3.connect('banks.db')
    sqlite_create_table_query='''CREATE TABLE customers(
                               name Text NOT NULL,
                               account_num integer,
                               amount_to_withdraw integer);'''
    cursor=sqliteconnection.cursor()
    print("Successfully connected to sqlite")
    cursor.execute(sqlite_create_table_query)
    sqliteconnection.commit()
    print("Sqlite table created")
    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table",error)

#  Inserting values in table
try:
    sqliteconnection=sqlite3.connect('banks.db')
    cursor=sqliteconnection.cursor()
    print("Successfully connected to sqlute")

    sqlite_insert_query=("""INSERT INTO customer
                        (name,account_num,amount_to_withdraw) VALUES(:name,:account_num,:amount_to_withdraw)""",{
                            'name':name.get(),
                            'account_num':account_num.get(),
                            'amount_to_withdraw':amount_to_withdraw.get()
                        })
    messagebox.showinfo("customers", "Successfully withdrawal")
    # count=cursor.execute(sqlite_insert_query)
    sqliteconnection.commit()
    # print("Record inserted successfully")
    sqliteconnection.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table")


        
# Deposite_btn=Button(root,text="Withdraw", fg="white", bg="blue2",font=("Verdana Bold", 14))
# Deposite_btn.grid(row=10,column=1)


root.mainloop()


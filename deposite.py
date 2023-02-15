from tkinter import *
from tkinter import messagebox
from time import strftime,gmtime
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title("Deposite money")
root["background"]="light green"


#   =========================== CREATING DB TABLE ========================

# try:
#     # Giving database name
#     main_database = sqlite3.connect('bank.db')

#     # Initializing cursor
#     c = main_dat abase.cursor()

#     # Creating customer table
#     c.execute("""CREATE TABLE customer(
#                 name text,
#                 account_number integer,
#                 amount integer
#     )
#     """)
#     print('Table created for Customer.')

#     # Committing and closing the database.
#     main_database.commit()
#     main_database.close()

# except sqlite3.Error as error:
#         print("Could not create DB customer") 


def depositeAmount():
    try:
        main_database = sqlite3.connect('bank.db')
        print("DB Connected")
        c = main_database.cursor()
        # Adding to database
        c.execute(
            "INSERT INTO customer VALUES(:name, :account_number,:amount)",
            {
                'name': name.get(),
                'account_number': account_num.get(),
                'amount': amount_to_deposit.get()
            })
        print('Deposited sucessfully')
        
        main_database.commit()
        main_database.close()
        name.delete(0,END)
        account_num.delete(0,END)
        amount_to_deposit.delete(0,END)

    except sqlite3.Error as error:
        print("Failed to despoite amount")

welcome=Label(root, text="Enter customer details to Deposit ", font=("Verdana Bold", 12),bg="oldlace", fg="blue2")
welcome.grid(row=0,column=0)

frame2 = Frame(root,bg="white",height=300,width=800)
frame2.grid(row=1,column=8,rowspan=4,columnspan=4,pady=30,padx=40)

img = Image.open("deposite.png")

bank_img = ImageTk.PhotoImage(img)
label_img = Label(frame2,image=bank_img).grid(row=0,column=0)

name=Entry(root,width=30)
name.grid(row=1,column=1)

account_num=Entry(root,width=30)
account_num.grid(row=2,column=1)

amount_to_deposit=Entry(root,width=30)
amount_to_deposit.grid(row=3,column=1)

name_label=Label(root,text="Name")
name_label.grid(row=1,column=0)

account_num_label=Label(root,text="Account Number")
account_num_label.grid(row=2,column=0)

amount_to_deposit_label=Label(root,text="Amount to deposit")
amount_to_deposit_label.grid(row=3,column=0)


Deposite_btn=Button(root,text="Deposite", fg="white", bg="blue2",font=("Verdana Bold", 14), command=depositeAmount)
Deposite_btn.grid(row=5,column=1)


root.mainloop()
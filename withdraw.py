from tkinter import *
from tkinter import messagebox
from time import strftime,gmtime
from PIL import ImageTk, Image
import mysql.connector
root=Tk()
root.title("Withdraw money")
global Name
global Account_number
global Withdraw_by
global Amount_to_withdraw

# import mysql.connector as c
# con=c.connect(host="localhost",
#        user="root",
#        password="misheel123",
#        database="Bank")
# cursor=con.cursor()
# name=input("enter name")
# account_num=int(input("enter account number"))
# withdraw_by=input("enter withdrawer name")
# amount_to_withdraw=int(input("enter the amount to withdraw"))

# query="Insert into customer(name,account_num,withdraw_by,amount_to_withdraw) values('{}',{},'{}',{})".format(name,account_num,withdraw_by,amount_to_withdraw)

# cursor.execute(query)
# con.commit()

# print("Data inserted")


        




welcome=Label(root, text="Enter customer details to Withdraw ", font=("Verdana Bold", 12),bg="oldlace", fg="blue2")
welcome.grid(row=0,column=0)
# welcome_frame=Frame(root,bg="#0096FF",height=20,width=20)
# welcome_frame.grid(row=0,column=0)

frame2 = Frame(root,bg="white",height=400,width=400)
frame2.grid(row=1,column=3,rowspan=4,columnspan=1)

img = Image.open("image/withdraw.png")
# img = img.resize((,600))     #resizing image
bank_img = ImageTk.PhotoImage(img)
label_img = Label(frame2,image=bank_img).grid(row=0,column=0)

name_entry=Entry(root,width=30)
name_entry.grid(row=1,column=1)

account_num=Entry(root,width=30)
account_num.grid(row=2,column=1)

withdraw_by=Entry(root,width=30)
withdraw_by.grid(row=3,column=1)

amount_to_withdraw=Entry(root,width=30)
amount_to_withdraw.grid(row=4,column=1)

name_label=Label(root,text="Name")
name_label.grid(row=1,column=0)

account_num_label=Label(root,text="Account Number")
account_num_label.grid(row=2,column=0)

withdraw_by_label = Label(root, text="Withdraw By")
withdraw_by_label.grid(row=3,column=0)

amount_to_withdraw_label=Label(root,text="Amount to Withdraw")
amount_to_withdraw_label.grid(row=4,column=0)

Deposite_btn=Button(root,text="Withdraw", fg="white", bg="blue2",font=("Verdana Bold", 14))
Deposite_btn.grid(row=10,column=1)


root.mainloop()
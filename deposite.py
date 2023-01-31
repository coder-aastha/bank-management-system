from tkinter import *
from tkinter import messagebox
from time import strftime,gmtime
from PIL import ImageTk,Image

root=Tk()
root.title("Deposite money")
root["background"]="light green"

welcome=Label(root, text="Enter customer details to Deposit ", font=("Verdana Bold", 12),bg="oldlace", fg="blue2")
welcome.grid(row=0,column=0)
# welcome_frame=Frame(root,bg="#0096FF",height=20,width=20)
# welcome_frame.grid(row=0,column=0)

frame2 = Frame(root,bg="white",height=300,width=800)
frame2.grid(row=1,column=8,rowspan=4,columnspan=4,pady=30,padx=40)

img = Image.open("image/deposite.png")
# img = img.resize((,600))     #resizing image
bank_img = ImageTk.PhotoImage(img)
label_img = Label(frame2,image=bank_img).grid(row=0,column=0)

name_entry=Entry(root,width=30)
name_entry.grid(row=1,column=1)

account_num=Entry(root,width=30)
account_num.grid(row=2,column=1)

deposited_by=Entry(root,width=30)
deposited_by.grid(row=3,column=1)

amount_to_deposit=Entry(root,width=30)
amount_to_deposit.grid(row=4,column=1)

name_label=Label(root,text="Name")
name_label.grid(row=1,column=0)

account_num_label=Label(root,text="Account Number")
account_num_label.grid(row=2,column=0)

deposited_by_label = Label(root, text="Deposited by")
deposited_by_label.grid(row=3,column=0)

amount_to_deposit_label=Label(root,text="Amount to deposit")
amount_to_deposit_label.grid(row=4,column=0)

Deposite_btn=Button(root,text="Deposite", fg="white", bg="blue2",font=("Verdana Bold", 14))
Deposite_btn.grid(row=5,column=1)


root.mainloop()
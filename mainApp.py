from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from time import strftime,gmtime
import sqlite3
root = Tk()
root.geometry("1944x1080")
root["background"] = "#5800FF"
root.title("Bank Management System")


def withdraw():
    root=Toplevel()
    root.title("Withdraw money")
    # global Name
    # global Account_number
    # global Withdraw_by
    # global Amount_to_withdraw

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

    img = Image.open("/image/bank.jpg")
    # img = img.resize((,600))     #resizing image
    bank_img = ImageTk.PhotoImage(img)
    global label_img
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

def customer_page_open():
    global customer_page
    global customer_features_frame
    customer_page.geometry("1100x740")
    customer_page["background"] = "#86E5FF"

    customer_features_frame = Frame(customer_page,bg="#86E5FF",height=750,width=400)
    customer_features_frame.grid(row=0,column=0,padx=20,pady=20)

    deposit_button = Button(customer_features_frame,text="Deposit",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24,command=deposit)
    deposit_button.grid(row=0,column=0)

    withdraw_button = Button(customer_features_frame,text="Withdraw",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24,command=withdraw)
    withdraw_button.grid(row=1,column=0,pady=20)

    balance_enquiry_button = Button(customer_features_frame,text="Balance enquiry",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24,command=balance_enquiry)
    balance_enquiry_button.grid(row=2,column=0,pady=1)

    customer_image_frame = Frame(customer_page,bg="#86E5FF",height=700,width=600)
    customer_image_frame.grid(row=0,column=5,padx=10,pady=0)

    customer_img1 = Image.open("image/customer_image.jpg")
    customer_img1 = customer_img1.resize((720,700))     #resizing image
    customer_img = ImageTk.PhotoImage(customer_img1)
    global label_customer_img
    label_customer_img = Label(customer_image_frame,image=customer_img).grid(row=0,column=8,padx=50)

def deposit():
    root=Toplevel()
    root.title("Deposite money")
    root["background"]="light green"

    welcome=Label(root, text="Enter customer details to Deposit ", font=("Verdana Bold", 12),bg="oldlace", fg="blue2")
    welcome.grid(row=0,column=0)
    # welcome_frame=Frame(root,bg="#0096FF",height=20,width=20)
    # welcome_frame.grid(row=0,column=0)

    frame2 = Frame(root,bg="white",height=300,width=800)
    frame2.grid(row=1,column=8,rowspan=4,columnspan=4,pady=30,padx=40)

    img = Image.open("deposite.png")
    # img = img.resize((,600))     #resizing image
    bank_img = ImageTk.PhotoImage(img)
    global label_img_deposit
    label_img_deposit = Label(frame2,image=bank_img)
    label_img_deposit.grid(row=0,column=0)

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

    Deposit_btn=Button(root,text="Deposite", fg="white", bg="blue2",font=("Verdana Bold", 14))
    Deposit_btn.grid(row=5,column=1)

def admin_login():
    #login page
    root=Toplevel()
    root.title('LOGIN')
    root.geometry('925x500+300+200')
    root.configure(bg='#fff')

    def submit():
    #create a databases or connect to one
        conn=sqlite3.connect('login_book.db')

        #create cursor
        c=conn.cursor()

        #Insert into table
        c.execute("INSERT INTO address VALUES (:username, :password)",{
            'username':user.get(),
            'password':code.get()
        })

        #showinfo messagebox
        messagebox.showinfo("Login", "Login Sucessful")

        conn.commit()

        conn.close()

    #function for checking the entered username and password
    def signin():
        username= user.get()
        password= code.get()

        if username=='admin' and password=='root':
            admin_page = Toplevel()
            admin_page.geometry("1100x750")
            admin_page["background"] = "#86E5FF"
            admin_features_frame = Frame(admin_page,bg="#86E5FF",height=750,width=400)
            admin_features_frame.grid(row=0,column=0,padx=20,pady=20)
            open_acc_button = Button(admin_features_frame,text="Opening Account",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24)
            open_acc_button.grid(row=0,column=0)
            cus_details_button = Button(admin_features_frame,text="Showing Customer Details",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24)
            cus_details_button.grid(row=1,column=0,pady=20)
            closing_acc_button = Button(admin_features_frame,text="Closing Account",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24)
            closing_acc_button.grid(row=2,column=0,pady=2)

            admin_image_frame = Frame(admin_page,bg="#86E5FF",height=700,width=600)
            admin_image_frame.grid(row=0,column=5,padx=10,pady=0)

            img_of_admin = Image.open("admin_img.png")
            img_of_admin = img_of_admin.resize((720,700))     #resizing image
            admin_img = ImageTk.PhotoImage(img_of_admin)
            global admin_img_label
            admin_img_label = Label(admin_image_frame,image=admin_img)
            admin_img_label.grid(row=0,column=8,padx=50)

        elif username!='admin' and password!='root':
            messagebox.showerror("Invalid","Invalid username and password")

        elif password!='root':
            messagebox.showerror("Invalid", "Invalid Password")

        elif username!='admin':
            messagebox.showerror("Invalid", "Invalid Username")

    #mainframe
    mainframe= Frame(root, bg='#fff')
    mainframe.grid(row=0,column=0)

    #subframe1
    logo=Frame(mainframe,width=450,height=500,bg='#3cdfff')
    logo.grid(row=0, column=0)

    #subframe2
    frame=Frame(mainframe,width=600,height=500,padx=180 ,bg='#fff')
    frame.grid(row=0,column=1)

    #heading for Subframe2
    heading= Label(frame,text='Login' ,fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.grid(row=0, column=0, padx=10,pady=20)


    #entry username
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')

    user=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user.grid(row=2,column=0, pady=10, ipadx=5,ipady=5, padx=1)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    #entry for password
    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')

    code= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    code.grid(row=3,column=0, pady=10, ipadx=5, ipady=5)
    code.insert(0,'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)


    #login button
    btn=Button(frame,width=25, pady=7, text='Log In', bg='#57a1f8',fg='white',border=0, command=signin)
    btn.grid(row=4, column=0)

    #text
    label=Label(frame,text="Don't have an account? ", fg='black',bg='white', font=('Microsoft YaHei UI Light', 9))
    label.grid(row=5, column=0)

    #sign up button
    sign_up=Button(frame, width=20,pady=7, text='Sign Up',border=0, bg='#57a1f8', cursor='hand2', fg='white')
    sign_up.grid(row=6, column=0)


def admin_page_open():
    admin_page = Toplevel()
    admin_page.geometry("1100x750")
    admin_page["background"] = "#86E5FF"
    admin_features_frame = Frame(admin_page,bg="#86E5FF",height=750,width=400)
    admin_features_frame.grid(row=0,column=0,padx=20,pady=20)
    open_acc_button = Button(admin_features_frame,text="Opening Account",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24)
    open_acc_button.grid(row=0,column=0)
    cus_details_button = Button(admin_features_frame,text="Showing Customer Details",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24)
    cus_details_button.grid(row=1,column=0,pady=20)
    closing_acc_button = Button(admin_features_frame,text="Closing Account",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24)
    closing_acc_button.grid(row=2,column=0,pady=2)

    admin_image_frame = Frame(admin_page,bg="#86E5FF",height=700,width=600)
    admin_image_frame.grid(row=0,column=5,padx=10,pady=0)

    img_of_admin = Image.open("admin_img.png")
    img_of_admin = img_of_admin.resize((720,700))     #resizing image
    admin_img = ImageTk.PhotoImage(img_of_admin)
    global admin_img_label
    admin_img_label = Label(admin_image_frame,image=admin_img).grid(row=0,column=8,padx=50)


def register():
    root=Toplevel()
    root.title('REGISTER')
    root.geometry('925x500+300+200')
    root.configure(bg='#fff')

    #mainframe
    mainframe= Frame(root, bg="#fff")
    mainframe.grid(row=0,column=0)

    #subframe 1
    logo=Frame(mainframe,width=450,height=500,bg='#3cdfff')
    logo.grid(row=0,column=0)

    #subframe 2
    frame=Frame(mainframe,width=600,height=500,padx=180, bg='#fff')
    frame.grid(row=0, column=1)

    #the 
    heading= Label(frame,text='Sign Up', fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light', 20, 'bold'))
    heading.grid(row=0,column=0)


    #first name
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'First Name')


    user=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user.grid(row=1,column=0, pady=10, ipadx=5)
    user.insert(0,'First Name')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)


    #Last name
    def on_enter(e):
        user1.delete(0,'end')

    def on_leave(e):
        name=user1.get()
        if name=='':
            user1.insert(0,'Last Name')

    user1=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user1.grid(row=2,column=0 ,pady=10, ipadx=5)
    user1.insert(0,'Last Name')
    user1.bind('<FocusIn>', on_enter)
    user1.bind('<FocusOut>', on_leave)


    #father's name
    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
        name=code.get()
        if name=="":
            code.insert(0,"Father's Name")

    code= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    code.grid(row=3,column=0, pady=10, ipadx=5)
    code.insert(0,"Father's Name")
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    #gender
    def on_enter(e):
        code1.delete(0,'end')

    def on_leave(e):
        name=code1.get()
        if name=='':
            code1.insert(0,'Gender')

    code1= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    code1.grid(row=4,column=0, pady=10, ipadx=5)
    code1.insert(0,'Gender')
    code1.bind('<FocusIn>', on_enter)
    code1.bind('<FocusOut>', on_leave)


    #email
    def on_enter(e):
        code2.delete(0,'end')

    def on_leave(e):
        name=code2.get()
        if name=='':
            code.insert(0,'Email')

    code2= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    code2.grid(row=6,column=0, pady=10, ipadx=5)
    code2.insert(0,'Email')
    code2.bind('<FocusIn>', on_enter)
    code2.bind('<FocusOut>', on_leave)


    #mobile number
    def on_enter(e):
        confirm.delete(0,'end')

    def on_leave(e):
        name=confirm.get()
        if name=='':
            confirm.insert(0,'Mobile Number')

    confirm= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    confirm.grid(row=7,column=0, pady=10, ipadx=5)
    confirm.insert(0,'Mobile Number')
    confirm.bind('<FocusIn>', on_enter)
    confirm.bind('<FocusOut>', on_leave)


    #first name
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Enter a Username')


    user=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user.grid(row=8,column=0, pady=10, ipadx=5)
    user.insert(0,'Enter a Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    #first name
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Enter Password')


    user=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user.grid(row=9,column=0, pady=10, ipadx=5)
    user.insert(0,'Enter Password')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)


    #button for sign in
    signin= Button(frame, width=20,background='#3cdfff', text='Sign In',border=0, bg='#3cdfff', cursor='hand2', fg='white')
    signin.grid(row=11,column=0)

    #label for already have an account?
    acc=Label(frame,text="Already have an account? ", fg='#2c3e4c', bg='white', font=('Microsoft YaHei UI Light', 9))
    acc.grid(row=12,column=0)

    #button for login
    login= Button(frame, width=15, text='Log In',border=0, bg='#3cdfff', cursor='hand2', fg='white',command=admin_login)
    login.grid(row=13,column=0)

#Making frames (frame 1)
# frame_welcome = Frame(root)
# frame_welcome.grid(row=0,column=0,pady=20)

def balance_enquiry():
    balance_enquiry = Toplevel()
    balance_enquiry.title("Balance Enquiry")
    balance_enquiry.geometry("700x200")
    balance_enquiry["background"] = "pink"
    balance_enquiry_label = Label(balance_enquiry,text="Your current balance is Rs. .......",font=("Code New Roman",24,"bold"),bg="pink")
    balance_enquiry_label.grid(row=3,column=2,pady=70,padx=20)
    balance_enquiry_button = Button(customer_features_frame,text="Balance Enquiry",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24,command=balance_enquiry)
    balance_enquiry_button.grid(row=2,column=0,pady=2)


def customer_login():
    #login page
    root=Toplevel()
    root.title('LOGIN')
    root.geometry('925x500+300+200')
    root.configure(bg='#fff')

    #function for checking the entered username and password
    def signin():
        username= user.get()
        password= code.get()

        if username=='admin' and password=='root':
        # def customer_page_open():
            global customer_page
            global customer_features_frame
            customer_page = Toplevel()
            customer_page.geometry("1100x740")
            customer_page["background"] = "#86E5FF"

            customer_features_frame = Frame(customer_page,bg="#86E5FF",height=750,width=400)
            customer_features_frame.grid(row=0,column=0,padx=20,pady=20)

            deposit_button = Button(customer_features_frame,text="Deposit",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24,command=deposit)
            deposit_button.grid(row=0,column=0)

            withdraw_button = Button(customer_features_frame,text="Withdraw",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24,command=withdraw)
            withdraw_button.grid(row=1,column=0,pady=20)

            balance_enquiry_button = Button(customer_features_frame,text="Balance enquiry",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24,command=balance_enquiry)
            balance_enquiry_button.grid(row=2,column=0,pady=1)

            customer_image_frame = Frame(customer_page,bg="#86E5FF",height=700,width=600)
            customer_image_frame.grid(row=0,column=5,padx=10,pady=0)

            customer_img1 = Image.open(file="D://finalProjectTkinter//bank-management-system//bank-management-system//image//customer_image.jpg")
            customer_img1 = customer_img1.resize((720,700))     #resizing image
            customer_img = ImageTk.PhotoImage(customer_img1)
            # global label_customer_img
            Label(customer_image_frame,image=customer_img).grid(row=0,column=8,padx=50)
        elif username!='admin' and password!='root':
            messagebox.showerror("Invalid","Invalid username and password")

        elif password!='root':
            messagebox.showerror("Invalid", "Invalid Password")

        elif username!='admin':
            messagebox.showerror("Invalid", "Invalid Username")

    #mainframe
    mainframe= Frame(root, bg='#fff')
    mainframe.grid(row=0,column=0)

    #subframe1
    logo=Frame(mainframe,width=450,height=500,bg='#3cdfff')
    logo.grid(row=0, column=0)

    #subframe2
    frame=Frame(mainframe,width=600,height=500,padx=180 ,bg='#fff')
    frame.grid(row=0,column=1)

    #heading for Subframe2
    heading= Label(frame,text='Login' ,fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.grid(row=0, column=0, padx=10,pady=20)


    #entry username
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')

    user=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user.grid(row=2,column=0, pady=10, ipadx=5,ipady=5, padx=1)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    #entry for password
    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')

    code= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    code.grid(row=3,column=0, pady=10, ipadx=5, ipady=5)
    code.insert(0,'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    #login button
    btn=Button(frame,width=25, pady=7, text='Log In', bg='#57a1f8',fg='white',border=0, command=signin)
    btn.grid(row=4, column=0,pady=10)


title_text = Label(root,text="WELCOME TO BANK",font=("Code New Roman",21,"bold"),bg="#00D7FF")
title_text.grid(row=0,column=9)

#frame 2
frame1 = Frame(root,bg="#0096FF",height=600,width=400)
frame1.grid(row=1,column=4,rowspan=4,columnspan=4,pady=70,padx=40)

#frame 3
frame2 = Frame(root,bg="white",height=600,width=800)
frame2.grid(row=1,column=8,rowspan=4,columnspan=4,pady=70,padx=40)

#adding image
#bank_image = ImageTk.PhotoImage(Image.open("Profile.png"))
img = Image.open("/image/bank.jpg")
img = img.resize((990,600))     #resizing image
bank_img = ImageTk.PhotoImage(img)
label_img = Label(frame2,image=bank_img).grid(row=0,column=0)

#Creating buttons
admin_button = Button(frame1,text="Admin",bg="#72FFFF",fg="black",font = ("Code New Roman",10,"bold"),height=10,width=20,command=register)
admin_button.grid(row=0,column=1,padx=100,pady=74)
# admin_button.
login_button = Button(frame1,text="Customer",bg="#72FFFF",fg="black",font= ("Code New Roman",10,"bold"),height=10,width=20,command=customer_login)
login_button.grid(row=1,column=1,pady=65)
login_button.grid(row=1,column=1,pady=65)
login_button.grid(row=1,column=1,pady=65)
login_button.grid(row=1,column=1,pady=65)


root.mainloop()
import random
import time
from tkinter import *
from tkinter import messagebox
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
import sqlite3
root = Tk()
root.geometry("1944x1080")
root["background"] = "#4A50E9"
root.title("Bank Management System")


def withdraw1():
    global label_img
    root = Toplevel()
    root.title("Withdraw money")
    root["background"] = "#86E5FF"

    welcome = Label(root, text="Enter customer details to Withdraw ", font=(
        "Verdana Bold", 12), bg="oldlace", fg="blue2")
    welcome.grid(row=0, column=0)

    frame2 = Frame(root, bg="white", height=300, width=800)
    frame2.grid(row=1, column=3, rowspan=4, columnspan=4, pady=30, padx=40)

    img = Image.open("withdraw.jpg")

    bank_img = ImageTk.PhotoImage(img)
    label_img = Label(frame2, image=bank_img).grid(row=0, column=0)

    name = Entry(root, width=30)
    name.grid(row=1, column=1)

    account_num = Entry(root, width=30)
    account_num.grid(row=2, column=1)

    amount_to_withdraw = Entry(root, width=30)
    amount_to_withdraw.grid(row=3, column=1)

    name_label = Label(root, text="Name")
    name_label.grid(row=1, column=0)

    account_num_label = Label(root, text="Account Number")
    account_num_label.grid(row=2, column=0)

    amount_to_withdraw_label = Label(root, text="Amount to Withdraw")
    amount_to_withdraw_label.grid(row=3, column=0)

    Withdraw_btn = Button(root, text="Withdraw", fg="white",
                          bg="blue2", font=("Verdana Bold", 14))
    Withdraw_btn.grid(row=10, column=1)


def admin_page_open():
    admin_page = Toplevel()
    admin_page.geometry("1100x750")
    admin_page["background"] = "#86E5FF"
    admin_features_frame = Frame(
        admin_page, bg="#86E5FF", height=750, width=400)
    admin_features_frame.grid(row=0, column=0, padx=20, pady=20)
    open_acc_button = Button(admin_features_frame, text="Opening Account", bg="#5BC0F8", font=(
        "Code New Roman", 10, "bold"), height=13, width=24)
    open_acc_button.grid(row=0, column=0)
    cus_details_button = Button(admin_features_frame, text="Showing Customer Details", bg="#5BC0F8", font=(
        "Code New Roman", 10, "bold"), height=13, width=24)
    cus_details_button.grid(row=1, column=0, pady=20)
    closing_acc_button = Button(admin_features_frame, text="Closing Account", bg="#5BC0F8", font=(
        "Code New Roman", 10, "bold"), height=13, width=24)
    closing_acc_button.grid(row=2, column=0, pady=2)

    amount_to_withdraw_label = Label(root, text="Amount to Withdraw")
    amount_to_withdraw_label.grid(row=3, column=0)

    Withdraw_btn = Button(root, text="Withdraw", fg="white",
                          bg="blue2", font=("Verdana Bold", 14))
    Withdraw_btn.grid(row=10, column=1)

# =============================================================================================
# =======================END OF CREATING WITHDRAW DASHBOARD SCREEN=============================
# =============================================================================================


# =============================================================================================
# =================================CREATING DEPOSIT DASHBOARD SCREEN===========================
# =============================================================================================

def deposit1():
    root = Toplevel()
    root.title("Deposite money")
    root["background"] = "light green"
    global name
    global depositeAmount

    def depositeAmount():
        try:
            main_database = sqlite3.connect('bank.db')
            print("DB Connected")
            c = main_database.cursor()
            # Adding to database
            c.execute(
                "INSERT INTO authentication VALUES(:name, :account_number,:amount)",
                {
                    'name': name.get(),
                    'account_number': account_num.get(),
                    'amount': amount_to_deposit.get()
                })
            messagebox.showinfo('sucess', 'Deposited sucessfully')

            main_database.commit()
            main_database.close()
            name.delete(0, END)
            account_num.delete(0, END)
            amount_to_deposit.delete(0, END)

        except sqlite3.Error as error:
            print("Failed to despoite amount")

    welcome = Label(root, text="Enter customer details to Deposit ", font=(
        "Verdana Bold", 12), bg="oldlace", fg="blue2")
    welcome.grid(row=0, column=0)
    # welcome_frame=Frame(root,bg="#0096FF",height=20,width=20)
    # welcome_frame.grid(row=0,column=0)

    frame2 = Frame(root, bg="white", height=300, width=800)
    frame2.grid(row=1, column=8, rowspan=4, columnspan=4, pady=30, padx=40)

    img = Image.open("deposite.png")
    # img = img.resize((,600))     #resizing image
    bank_img = ImageTk.PhotoImage(img)
    global label_img_deposit
    label_img_deposit = Label(frame2, image=bank_img)
    label_img_deposit.grid(row=0, column=0)

    name_entry = Entry(root, width=30)
    name_entry.grid(row=1, column=1)

    account_num = Entry(root, width=30)
    account_num.grid(row=2, column=1)

    amount_to_deposit = Entry(root, width=30)
    amount_to_deposit.grid(row=3, column=1)

    name_label = Label(root, text="Name")
    name_label.grid(row=1, column=0)

    account_num_label = Label(root, text="Account Number")
    account_num_label.grid(row=2, column=0)

    amount_to_deposit_label = Label(root, text="Amount to deposit")
    amount_to_deposit_label.grid(row=3, column=0)

    Deposit_btn = Button(root, text="Deposit", fg="white",
                         bg="blue2", font=("Verdana Bold", 14))
    Deposit_btn.grid(row=4, column=1)

    # messagebox.showinfo("Sucess","Deposited sucessfull")

# =============================================================================================
# ===========================END OF CREATING DEPOSIT DASHBOARD SCREEN==========================
# =============================================================================================


# =============================================================================================
# ============================CREATING BALANCE ENQUIRY DASHBOARD SCREEN========================
# =============================================================================================

def balanceEnquiryQuery():
    balance = account_no.get()

    if len(balance) == 0 or len(account_no) == 0:
        messagebox.showinfo("Warning", "Fields cannot be empty")
    else:
        try:
            main_database = sqlite3.connect('db/user.db')
            c = main_database.cursor()

            c.execute(
                "SELECT balance FROM user WHERE account_no = :account_no", {
                    "account_no": account_no,
                })
            accBalance = c.fetchone()[0]
            if int(balance) > accBalance:
                messagebox.showerror(
                    "Failed", "You Have insufficient Balance in your account please try again..")
            else:
                accBalance -= int(balance)
                c.execute("UPDATE user SET balance = :balance WHERE account_no = :account_no", {
                    "account_no": account_no,
                    "balance": accBalance
                })
                print(
                    f"Thanks for using our service. Remaining funds in your account = {accBalance}")
                messagebox.showinfo(
                    "Success", "Amount withdraw successfully")
            print(balance)

            main_database.commit()
            main_database.close()

        except sqlite3.Error as error:
            print(error)
            print("Could not withdraw balance")



def balance_enquiry():

    global balance_enquiry
    global account_num

    balance_enquiry = Toplevel()
    balance_enquiry.title("Balance Enquiry")
    balance_enquiry.geometry("600x300")
    balance_enquiry["background"] = "#5BC0F8"

    account_no = Label(
        balance_enquiry, text="Account Number")
    account_no.grid(row=0, column=0, pady=10)

    account_num = Entry(balance_enquiry, width=30)
    account_num.grid(row=1, column=0, pady=10)

    acNo = account_num.get()

    balance_enquiry_button = Button(balance_enquiry, text="Balance Enquiry", bg="white", font=(
        "Code New Roman", 10, "bold"), height=2, width=15, command=query)
    balance_enquiry_button.grid(row=2, column=0, pady=10)

 


def query():
    account_n = account_num.get()
    try:
        main_database = sqlite3.connect('db/user.db')
        c = main_database.cursor()

        c.execute(
                "SELECT balance FROM user WHERE account_no = :account_no", {
                    "account_no": account_n,
                })
        data  =  c.fetchone()
        # print("data to object " + data)
        balc = data[0]

        userBalance = str(balc)
        print("=====================")
        print( balc)
        print(data)

        main_database.commit()
        main_database.close()

    except sqlite3.Error as error:
        print(error)
        print("Could not get your balance")


    balance_enquiry_label = Label(balance_enquiry, text="Your current balance is Rs.", font=(
            "Code New Roman", 24, "bold"), bg="#5BC0F8")
    balance_enquiry_label.grid(row=3, column=0, pady=10, padx=20)

    balance = Label(balance_enquiry, text=userBalance, font=(
            "Code New Roman", 24, "bold"), bg="#5BC0F8")
    balance.grid(row=3, column=1, padx=10)

   
            

# =============================================================================================
# ======================END OF CREATING BALANCE ENQUIRY DASHBOARD SCREEN=======================
# =============================================================================================


# =============================================================================================
# ============================CREATING CUSTOMERS DASHBOARD SCREEN==============================
# =============================================================================================

def customerDashboard(username, account_no):
    global customer_page
    global customer_features_frame
    global customer_image_frame
    customer_page = Toplevel()
    customer_page.geometry("1100x740")
    customer_page["background"] = "#86E5FF"

    usrname = "Username " + username
    accno = "Account Number: " + account_no

    customer_features_frame = Frame(
        customer_page, bg="#86E5FF", height=750, width=400)
    customer_features_frame.grid(row=0, column=0, padx=20, pady=20)

    deposit_button = Button(customer_features_frame, text="Deposit", bg="#5BC0F8", font=(
        "Code New Roman", 10, "bold"), height=13, width=24, command=deposite)
    deposit_button.grid(row=0, column=0)

    withdraw_button = Button(customer_features_frame, text="Withdraw", bg="#5BC0F8", font=(
        "Code New Roman", 10, "bold"), height=13, width=24, command=withdraw)
    withdraw_button.grid(row=1, column=0, pady=20)

    balance_enquiry_button = Button(customer_features_frame, text="Balance enquiry", bg="#5BC0F8", font=(
        "Code New Roman", 10, "bold"), height=13, width=24, command=balance_enquiry)
    balance_enquiry_button.grid(row=2, column=0, pady=1)

    customer_image_frame = Frame(
        customer_page, bg="#86E5FF", height=700, width=600)
    customer_image_frame.grid(row=0, column=5, padx=10, pady=0)

    # details_label=Label(customer_image_frame,text=fullname)
    # details_label.grid(row=0,column=0, pady=10)

    details_label2 = Label(customer_image_frame, text=usrname)
    details_label2.grid(row=0, column=1, pady=10)

    details_label2 = Label(customer_image_frame, text=accno)
    details_label2.grid(row=0, column=2, pady=10)


# =============================================================================================
# ===========================END OF CREATING CUSTOMERS DASHBOARD SCREEN========================
# =============================================================================================


def deposite():
    global account_num
    global amount_to_deposite
    global account_no

    account_num_label = Label(customer_image_frame, text="Account Number")
    account_num_label.grid(row=2, column=0, pady=10)

    account_num = Entry(customer_image_frame, width=30)
    account_num.grid(row=3, column=0, pady=10)

    amount_to_deposite_label = Label(
        customer_image_frame, text="Amount to Deposite")
    amount_to_deposite_label.grid(row=4, column=0, pady=10)

    amount_to_deposite = Entry(customer_image_frame, width=30)
    amount_to_deposite.grid(row=5, column=0, pady=10)

    deposite_btn = Button(customer_image_frame, text="Make a Deposite",
                          fg="white", bg="blue2", font=("Verdana Bold", 14), command=depositeQuery)
    deposite_btn.grid(row=6, column=0, pady=10)


def depositeQuery():
    balance = amount_to_deposite.get()
    account_no = account_num.get()

    if len(balance) == 0 or len(account_no) == 0:
        messagebox.showinfo("Warning", "Fields cannot be empty")
    else:
        try:
            main_database = sqlite3.connect('db/user.db')
            c = main_database.cursor()

            c.execute(
                "SELECT balance FROM user WHERE account_no = :account_no", {
                    "account_no": account_no,
                })
            accBalance = c.fetchone()[0]

            accBalance += int(balance)
            c.execute("UPDATE user SET balance = :balance WHERE account_no = :account_no", {
                "account_no": account_no,
                "balance": accBalance
            })
            print(
                f"Thanks for using our service. New funds in your account = {accBalance}")
            messagebox.showinfo(
                "Success", "Amount deposited successfully")

            print(balance)

            main_database.commit()
            main_database.close()
        except sqlite3.Error as error:
            print(error)
            print("Could not make a deposite ")


def withdraw():
    global amount_to_withdraw
    global withdraw_account_num

    account_num_label = Label(customer_image_frame, text="Account Number")
    account_num_label.grid(row=2, column=0, pady=10)

    withdraw_account_num = Entry(customer_image_frame, width=30)
    withdraw_account_num.grid(row=3, column=0, pady=10)

    amount_to_withdraw_label = Label(
        customer_image_frame, text="Amount to Withdraw")
    amount_to_withdraw_label.grid(row=4, column=0, pady=10)

    amount_to_withdraw = Entry(customer_image_frame, width=30)
    amount_to_withdraw.grid(row=5, column=0, pady=10)

    withdraw_btn = Button(customer_image_frame, text="Withdraw Amount",
                          fg="white", bg="blue2", font=("Verdana Bold", 14), command=withdrawQuery)
    withdraw_btn.grid(row=6, column=0, pady=10)


def withdrawQuery():
    balance = amount_to_withdraw.get()
    account_no = withdraw_account_num.get()

    if len(balance) == 0 or len(account_no) == 0:
        messagebox.showinfo("Warning", "Fields cannot be empty")
    else:
        try:
            main_database = sqlite3.connect('db/user.db')
            c = main_database.cursor()

            c.execute(
                "SELECT balance FROM user WHERE account_no = :account_no", {
                    "account_no": account_no,
                })
            accBalance = c.fetchone()[0]
            if int(balance) > accBalance:
                messagebox.showerror(
                    "Failed", "You Have insufficient Balance in your account please try again..")
            else:
                accBalance -= int(balance)
                c.execute("UPDATE user SET balance = :balance WHERE account_no = :account_no", {
                    "account_no": account_no,
                    "balance": accBalance
                })
                print(
                    f"Thanks for using our service. Remaining funds in your account = {accBalance}")
                messagebox.showinfo(
                    "Success", "Amount withdraw successfully")
            print(balance)

            main_database.commit()
            main_database.close()

        except sqlite3.Error as error:
            print(error)
            print("Could not withdraw balance")


# =============================================================================================
# ============================== Customer Login Screen | Query ================================
# =============================================================================================

def customerLoginScreen():
    customerLogin = Toplevel()
    customerLogin.title('CUSTOMER LOGIN SCREEN - BANK APP')
    customerLogin.geometry('925x500+300+200')
    customerLogin.configure(bg='#fff')

    global username
    global password

    mainframe = Frame(customerLogin, bg='#fff')
    mainframe.grid(row=0, column=0)

    # subframe1
    logo = Frame(mainframe, width=450, height=500, bg='#3cdfff')
    logo.grid(row=0, column=0)

    # subframe2
    frame = Frame(mainframe, width=600, height=500, padx=180, bg='#fff')
    frame.grid(row=0, column=1)

    # heading for Subframe2
    heading = Label(frame, text='Login', fg='#57a1f8', bg='white',
                    font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.grid(row=0, column=0, padx=10, pady=20)

    # entry username

    def on_enter(e):
        username.delete(0, 'end')

    def on_leave(e):
        name = username.get()
        if name == '':
            username.insert(0, 'Username')

    username = Entry(frame, width=25, fg="black", border=1,
                     bg='white', font=('Microsoft YaHei UI Light', 11))
    username.grid(row=2, column=0, pady=10, ipadx=5, ipady=5, padx=1)
    username.bind('<FocusIn>', on_enter)
    username.bind('<FocusOut>', on_leave)

    # entry for password
    def on_enter(e):
        password.delete(0, 'end')

    def on_leave(e):
        name = password.get()
        if name == '':
            password.insert(0, 'Password')

    password = Entry(frame, width=25, fg='black', border=1,
                     bg='white', font=('Microsoft YaHei UI Light', 11))
    password.grid(row=3, column=0, pady=10, ipadx=5, ipady=5)
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)

    # login button
    btn = Button(frame, width=25, pady=7, text='Log In',
                 bg='#57a1f8', fg='white', border=0, command=customerLoginQuery)
    btn.grid(row=4, column=0)


def customerLoginQuery():
    user = username.get()
    psw = password.get()

    if len(user) == 0 or len(psw) == 0:
        messagebox.showinfo("Warning", "Fields cannot be empty")
    else:
        try:
            main_database = sqlite3.connect('db/user.db')
            c = main_database.cursor()

            c.execute(
                "SELECT * FROM user WHERE username = ? AND password = ?", (user, psw))
            data = c.fetchone()
            print(data)

            if data:
                for d in data:
                    print(d)
                customerDashboard(data[7], data[2])

            else:
                messagebox.showerror(
                    "Error", "No user found with this username and password.")

            main_database.commit()
            main_database.close()

        except sqlite3.Error as error:
            print(error)
            print("Could not login to the system")

# ================================================================================================
# ===================== End Customer Login Screen | Query ========================================
# ================================================================================================


# ================================================================================================
# ===============================Customer Register Screen | Query ================================
# ================================================================================================

def customerRegisterQuery():
    global fullname
    global fathername
    global account_no
    global gender
    global contact
    global account_type
    global balance
    global username
    global password

    fullname = fullname.get()
    fathername = fathername.get()
    gender = gender.get()
    contact = contact.get()
    usr = username.get()
    psw = password.get()

    account_number = random.randint(100000, 999999)

    userAccountNumber = "063418900"+str(account_number)
    print(userAccountNumber)

    if len(usr) == 0 or len(psw) == 0:
        messagebox.showerror("Error", "Fields cannot be empty")
    else:
        try:
            # create a databases or connect to one
            conn = sqlite3.connect('db/user.db')

            # create cursor
            c = conn.cursor()

            # Insert into table
            c.execute("INSERT INTO user(full_name, father_name, account_no, gender, contact, account_type, balance,username, password) VALUES (:full_name, :father_name, :account_no, :gender, :contact, :account_type,:balance, :username, :password)", {
                'full_name': fullname,
                'father_name': fathername,
                'account_no': userAccountNumber,
                'gender': gender,
                'contact': contact,
                'account_type': "Savings",
                'balance': "0",
                'username': usr,
                'password': psw
            })

            # showinfo messagebox
            print("Customer Registered Successfully")
            messagebox.showinfo("Customer account creation",
                                "Customer account created successfully")

            conn.commit()
            conn.close()

        except sqlite3.Error as error:
            print(error)
            print("Could not create an account for customer.")
            messagebox.showinfo("Error", "Something went wrong.")


def customerRegisterScreen():
    global fullname
    global fathername
    global account_no
    global gender
    global contact
    global account_type
    global balance
    global username
    global password

    root = Toplevel()
    root.title("CUSTOMER REGISTER - BANKING APP")
    root.geometry('925x500+500+200')
    root.configure(bg='#fff')

    # mainframe
    mainframe = Frame(root, bg="#fff")
    mainframe.grid(row=0, column=0)

    # subframe 1
    logo = Frame(mainframe, width=450, height=500, bg='#3cdfff')
    logo.grid(row=0, column=0)

    # subframe 2
    frame = Frame(mainframe, width=600, height=500, padx=180, bg='#fff')
    frame.grid(row=0, column=1)

    # the
    heading = Label(frame, text='Create customer account', fg='#57a1f8',
                    bg='white', font=('Microsoft YaHei UI Light', 20, 'bold'))
    heading.grid(row=0, column=0)

    # full name

    def on_enter(e):
        fullname.delete(0, 'end')

    def on_leave(e):
        name = fullname.get()
        if name == '':
            fullname.insert(0, 'Enter Full Name')

    fullname = Entry(frame, width=25, fg="black", border=1,
                     bg='white', font=('Microsoft YaHei UI Light', 11))
    fullname.grid(row=1, column=0, pady=10, ipadx=5)
    fullname.insert(0, 'Enter Full Name')
    fullname.bind('<FocusIn>', on_enter)
    fullname.bind('<FocusOut>', on_leave)

    # Father's name

    def on_enter(e):
        fathername.delete(0, 'end')

    def on_leave(e):
        name = fathername.get()
        if name == '':
            fathername.insert(0, "Father's Name")

    fathername = Entry(frame, width=25, fg="black", border=1,
                       bg='white', font=('Microsoft YaHei UI Light', 11))
    fathername.grid(row=2, column=0, pady=10, ipadx=5)
    fathername.insert(0, "Father's Name")
    fathername.bind('<FocusIn>', on_enter)
    fathername.bind('<FocusOut>', on_leave)

    # Gender

    def on_enter(e):
        gender.delete(0, 'end')

    def on_leave(e):
        name = gender.get()
        if name == "":
            gender.insert(0, "Gender")

    gender = Entry(frame, width=25, fg='black', border=1,
                   bg='white', font=('Microsoft YaHei UI Light', 11))
    gender.grid(row=3, column=0, pady=10, ipadx=5)
    gender.insert(0, "Gender")
    gender.bind('<FocusIn>', on_enter)
    gender.bind('<FocusOut>', on_leave)

    # Account No
    def on_enter(e):
        account_no.delete(0, 'end')

    def on_leave(e):
        name = account_no.get()
        if name == '':
            account_no.insert(0, 'Account No')

    account_no = Entry(frame, width=25, fg='black', border=1,
                       bg='white', font=('Microsoft YaHei UI Light', 11))
    account_no.grid(row=4, column=0, pady=10, ipadx=5)
    account_no.insert(0, 'Account No')
    account_no.bind('<FocusIn>', on_enter)
    account_no.bind('<FocusOut>', on_leave)

    # Mobile Number

    def on_enter(e):
        contact.delete(0, 'end')

    def on_leave(e):
        name = contact.get()
        if name == '':
            contact.insert(0, 'Mobile Number')

    contact = Entry(frame, width=25, fg='black', border=1,
                    bg='white', font=('Microsoft YaHei UI Light', 11))
    contact.grid(row=6, column=0, pady=10, ipadx=5)
    contact.insert(0, 'Mobile Number')
    contact.bind('<FocusIn>', on_enter)
    contact.bind('<FocusOut>', on_leave)

    def on_enter(e):
        username.delete(0, 'end')

    def on_leave(e):
        name = username.get()
        if name == '':
            username.insert(0, 'Enter a Username')

    username = Entry(frame, width=25, fg="black", border=1,
                     bg='white', font=('Microsoft YaHei UI Light', 11))
    username.grid(row=8, column=0, pady=10, ipadx=5)
    username.bind('<FocusIn>', on_enter)
    username.bind('<FocusOut>', on_leave)

    # Password entry

    def on_enter(e):
        password.delete(0, 'end')

    def on_leave(e):
        name = password.get()
        if name == '':
            password.insert(0, 'Enter Password')

    password = Entry(frame, width=25, fg="black", border=1,
                     bg='white', font=('Microsoft YaHei UI Light', 11))
    password.grid(row=9, column=0, pady=10, ipadx=5)
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)

    # button for sign in
    signupCustomer = Button(frame, width=20, background='#3cdfff', text='Register Customer',
                            border=0, bg='#3cdfff', cursor='hand2', fg='black', command=customerRegisterQuery)
    signupCustomer.grid(row=11, column=0)


# ================================================================================================
# ============================= End  Customer Register Screen | Query ============================
# ================================================================================================

def close_account():
    usrname = register_ID.get()
    print(usrname)

    conn = sqlite3.connect('db/user.db')

    cursor = conn.cursor()

    cursor.execute("DELETE from user WHERE account_no = " + register_ID.get() )


    conn.commit()
    conn.close()

    message = "Account deleted successfully."
    messagebox.showinfo("Delete Account", message)



def closeCustomerAccount():
    global register_ID

    root=Toplevel()
    root.title('CLOSE ACCOUNT - BANK APP')
    root.geometry('925x500+300+200')
    root.configure(bg='#fff')

    frame = Frame(root, bd=2, bg='lightpink', relief=SOLID, padx=5, pady=20, height=200, width=200)
    frame.grid(row=1, column=1, padx=400, pady=95, ipadx=20, ipady=30)

    Label(frame, text="username", bg='grey').grid(row=0, column=0, sticky=W, pady=50, padx=3)

    Delete_btn = Button(frame, width=15, text='DELETE', bg='grey', font=("f"), cursor='hand2', command= close_account)
    register_ID = Entry(frame, font=("f"))

    register_ID.grid(row=0, column=1, pady=10, padx=20)
    Delete_btn.grid(row=1, column=1, pady=10, padx=20)


# ================================================================================================
# ============================= View All Customers ============================
# ================================================================================================

def showCustomerInformation():
    root = Toplevel()
    root.geometry('1500x900')
    root.title('Bank Management System - Show All Customers')
    root['background'] = '#304562'
    # root.iconbitmap('C:/Users/ENVY/PycharmProjects/StoreManagementSystem/images/store.ico')

    # Creating frame for tree view
    tree_frame = Frame(root, bg='#304562')
    tree_frame.pack(pady=7, padx=5)

    back_home_btn = Button(tree_frame, bg='#304562', text='❮', relief=FLAT, fg='#f7f7f7', padx=20,
                           font=('HandVetica', 21), command=lambda: root.destroy())
    back_home_btn.place(x=30)

    title = Label(tree_frame, text="All Customer Information",
                  bg='#304562', fg='#f7f7f7', font=('HandVetica', 37))
    title.pack(side=TOP, padx=80)

    # Creating clock
    def clock():
        hour = time.strftime('%I')
        minute = time.strftime('%M')
        second = time.strftime('%S')
        unit = time.strftime('%p')

        show_time.config(text=hour + ':' + minute + ':' + second + ':' + unit)
        show_time.after(1000, clock)

    # Displaying time
    show_time = Label(tree_frame, bg='#304562', fg='#f7f7f7',
                      text="", font=('digital-7', 22), padx=50)
    show_time.place(x=1200, y=20)
    clock()

    # Adding style
    style = ttk.Style()

    # Choosing theme  equilux bg='#091b33'
    style.theme_use('classic')

    # Configure the tree color
    style.configure("Treeview",
                    background='#091b33',
                    foreground='black',
                    rowheight=40,
                    fieldbackground='#091b33')

    # Configure Font name and Size
    style.configure("Treeview", font=('Code New Roman', 13))
    style.configure("Treeview.Heading", font=('Code New Roman', 15))

    # Change selected color
    style.map('Treeview',
              background=[('selected', '#06e6b0')])

    # Creating a Tree view Scrollbar Vertical

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Creating a Tree view Scrollbar Horizontal

    tree_scroll_horizontal = Scrollbar(tree_frame, orient=HORIZONTAL)
    tree_scroll_horizontal.pack(side=BOTTOM, fill=X)

    # Create the Tree view
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended',
                           xscrollcommand=tree_scroll_horizontal.set)
    my_tree.pack(pady=40)

    # configure scrollbar
    tree_scroll.config(command=my_tree.yview)
    tree_scroll_horizontal.config(command=my_tree.xview)

    # Data from database
    # ------------------------------------------------------------------------------------------------
    # connecting database to tree view
    def connect():
        main_database = sqlite3.connect("storemanagement.db")

        cursor = main_database.cursor()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS showdata (billno INTEGER PRIMARY KEY, productname TEXT, productquantity TEXT, productrate TEXT, totalprice TEXT, companyname TEXT, address TEXT, contactnumber TEXT, email TEXT, date TEXT, productdescription TEXT)")

        main_database.commit()
        main_database.close()

    # Showing data at tree view from database
    def View():
        main_database = sqlite3.connect("db/user.db")

        cursor = main_database.cursor()

        cursor.execute("SELECT * FROM user")

        rows = cursor.fetchall()

        count = 0

        # To loop through database data
        for row in rows:
            if count % 2 == 0:
                my_tree.insert("", END, values=row, tags=('evenrow',))
            else:
                my_tree.insert("", END, values=row, tags=('oddrow',))
            count += 1

        main_database.close()

    # Define column

    my_tree['columns'] = (
        'Full Name', 'Father Name', 'Account Number', 'Gender', 'Contact Number', 'Account Type', 'Account Balance',
        'Username', 'Password')

    # Format column
    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('Full Name', anchor=CENTER, width=100)
    my_tree.column('Father Name', anchor=CENTER, width=160)
    my_tree.column('Account Number', anchor=CENTER, width=210)
    my_tree.column('Gender', anchor=CENTER, width=160)
    my_tree.column('Contact Number', anchor=CENTER, width=160)
    my_tree.column('Account Type', anchor=CENTER, width=200)
    my_tree.column('Account Balance', anchor=CENTER, width=160)
    my_tree.column('Username', anchor=CENTER, width=190)
    my_tree.column('Password', anchor=CENTER, width=250)

    # Create Heading
    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('Full Name', text='Full Name', anchor=CENTER)
    my_tree.heading('Father Name', text='Father Name', anchor=CENTER)
    my_tree.heading('Account Number', text='Account Number', anchor=CENTER)
    my_tree.heading('Gender', text='Gender', anchor=CENTER)
    my_tree.heading('Contact Number', text='Contact Number', anchor=CENTER)
    my_tree.heading('Account Type', text='Account Type', anchor=CENTER)
    my_tree.heading('Account Balance', text='Account Balance', anchor=CENTER)
    my_tree.heading('Username', text='Username', anchor=CENTER)
    my_tree.heading('Password', text='Password', anchor=CENTER)

    # Create Striped Row Tag
    my_tree.tag_configure('oddrow', background='white')
    my_tree.tag_configure('evenrow', background='#fcf1f1')

    # Button to show data

    button1 = Button(tree_frame, text="View data", bg="#06e6b0", padx=20, pady=20, fg="#091b33",
                     font=('Code New Roman', 21),
                     command=View)
    button1.pack(pady=60)


def adminDashboard():
    adminLogin.destroy()
    global admin_img_label
    admin_page = Toplevel()
    admin_page.title("Bank Management System - Admin Dashboard")
    admin_page.geometry("1100x750")
    admin_page["background"] = "#86E5FF"
    admin_features_frame = Frame(
        admin_page, bg="#86E5FF", height=750, width=400)
    admin_features_frame.grid(row=0, column=0, padx=20, pady=20)

    open_acc_button = Button(admin_features_frame, text="Create Customer Account", bg="#5BC0F8", font=(
        "Code New Roman", 10, "bold"), height=13, width=24, command=customerRegisterScreen)
    open_acc_button.grid(row=0, column=0)

    cus_details_button = Button(admin_features_frame, text="Show All Customer", bg="#5BC0F8", font=(
        "Code New Roman", 10, "bold"), height=13, width=24, command=showCustomerInformation)
    cus_details_button.grid(row=1, column=0, pady=20)

    closing_acc_button = Button(admin_features_frame, text="Close Account", bg="#5BC0F8", font=(
        "Code New Roman", 10, "bold"), height=13, width=24, command=closeCustomerAccount)
    closing_acc_button.grid(row=2, column=0, pady=2)

    def log_out():
        message = messagebox.askquestion(
            'Logout', 'Do you want to logout ?', parent=admin_page)
        if message == 'yes':
            admin_page.destroy()
        elif message == 'no':
            admin_page.mainloop()

    logout = Button(admin_features_frame, text="Logout", bg="#5BC0F8", font=(
        "Code New Roman", 10, "bold"), height=6, width=6, command=log_out)
    logout.grid(row=3, column=0, pady=2)

    admin_image_frame = Frame(admin_page, bg="#86E5FF", height=700, width=600)
    admin_image_frame.grid(row=0, column=5, padx=10, pady=0)

    img_of_admin = Image.open("admin_img.png")
    img_of_admin = img_of_admin.resize((720, 700))  # resizing image
    admin_img = ImageTk.PhotoImage(img_of_admin)
    admin_img_label = Label(admin_image_frame, image=admin_img).grid(
        row=0, column=8, padx=50)

    admin_page.mainloop()

# ================================================================================================
# =========================== Admin Login Screen | Query =========================================
# ================================================================================================


def adminLoginScreen():

    global username
    global password
    global adminLogin

    adminLogin = Toplevel()
    adminLogin.title('ADMIN LOGIN SCREEN - BANK APP')
    adminLogin.geometry('925x500+300+200')
    adminLogin.configure(bg='#fff')

    mainframe = Frame(adminLogin, bg='#fff')
    mainframe.grid(row=0, column=0)

    # subframe1
    logo = Frame(mainframe, width=450, height=500, bg='#3cdfff')
    logo.grid(row=0, column=0)

    # subframe2
    frame = Frame(mainframe, width=600, height=500, padx=180, bg='#fff')
    frame.grid(row=0, column=1)

    # heading for Subframe2
    heading = Label(frame, text='Login', fg='#57a1f8', bg='white',
                    font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.grid(row=0, column=0, padx=10, pady=20)

    # entry username

    def on_enter(e):
        username.delete(0, 'end')

    def on_leave(e):
        name = username.get()
        if name == '':
            username.insert(0, 'Username')

    username = Entry(frame, width=25, fg="black", border=1,
                     bg='white', font=('Microsoft YaHei UI Light', 11))
    username.grid(row=2, column=0, pady=10, ipadx=5, ipady=5, padx=1)
    username.bind('<FocusIn>', on_enter)
    username.bind('<FocusOut>', on_leave)

    # entry for password
    def on_enter(e):
        password.delete(0, 'end')

    def on_leave(e):
        name = password.get()
        if name == '':
            password.insert(0, 'Password')

    password = Entry(frame, width=25, fg='black', border=1,
                     bg='white', font=('Microsoft YaHei UI Light', 11))
    password.grid(row=3, column=0, pady=10, ipadx=5, ipady=5)
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)

    # login button
    btn = Button(frame, width=25, pady=7, text='Log In',
                 bg='#57a1f8', fg='white', border=0, command=adminLoginQuery)
    btn.grid(row=4, column=0)

    # text
    label = Label(frame, text="Don't have an account? ", fg='black',
                  bg='white', font=('Microsoft YaHei UI Light', 9))
    label.grid(row=5, column=0)

    # sign up button
    sign_up = Button(frame, width=20, pady=7, text='Sign Up', border=0,
                     bg='#57a1f8', cursor='hand2', fg='white', command=adminRegisterScreen)
    sign_up.grid(row=6, column=0)

    # adminLogin.mainloop()
    # adminLogin.destroy()


def adminLoginQuery():
    user = username.get()
    psw = password.get()
    role = 1

    if len(user) == 0 or len(psw) == 0:
        messagebox.showinfo("Warning", "Fields cannot be empty")
    else:
        try:
            main_database = sqlite3.connect('db/admin.db')
            c = main_database.cursor()

            c.execute(
                "SELECT * FROM admin WHERE username = ? AND password = ? AND role = ? ", (user, psw, role))
            data = c.fetchone()

            if data:
                adminDashboard()
            else:
                messagebox.showerror(
                    "Error", "No user found with the given credentials!")

            main_database.commit()
            main_database.close()

        except sqlite3.Error as error:
            print("Something went wrong! Could not login to the system")


# ================================================================================================
# ============================== Admin Registration Screen | Query ===============================
# ================================================================================================


def adminRegisterScreen():
    global fullname
    global password
    global username
    global adminRegister

    adminRegister = Toplevel()
    adminRegister.title('ADMIN REGISTER - BANKING APP')
    adminRegister.geometry('925x500+300+200')
    adminRegister.configure(bg='#fff')

    # mainframe
    mainframe = Frame(adminRegister, bg="#fff")
    mainframe.grid(row=0, column=0)

    # subframe 1
    logo = Frame(mainframe, width=450, height=500, bg='#3cdfff')
    logo.grid(row=0, column=0)

    # subframe 2
    frame = Frame(mainframe, width=600, height=500, padx=180, bg='#fff')
    frame.grid(row=0, column=1)

    # the
    heading = Label(frame, text='Sign Up', fg='#57a1f8',
                    bg='white', font=('Microsoft YaHei UI Light', 20, 'bold'))
    heading.grid(row=0, column=0)

    fullname = Entry(frame, width=25, fg="black", border=1,
                     bg='white', font=('Microsoft YaHei UI Light', 11))
    fullname.grid(row=1, column=0, pady=10, ipadx=5)

    username = Entry(frame, width=25, fg="black", border=1,
                     bg='white', font=('Microsoft YaHei UI Light', 11))
    username.grid(row=6, column=0, pady=10, ipadx=5)

    password = Entry(frame, width=25, fg="black", border=1,
                     bg='white', font=('Microsoft YaHei UI Light', 11))
    password.grid(row=7, column=0, pady=10, ipadx=5)

    # button for sign in
    signin = Button(frame, width=20, background='#3cdfff', text='Register', border=0,
                    bg='#3cdfff', cursor='hand2', fg='white', command=adminRegisterQuery)
    signin.grid(row=10, column=0)

    # label for already have an account?
    acc = Label(frame, text="Already have an account? ", fg='#2c3e4c',
                bg='white', font=('Microsoft YaHei UI Light', 9))
    acc.grid(row=11, column=0)

    # button for login
    login = Button(frame, width=15, text='Log In', border=0, bg='#3cdfff',
                   cursor='hand2', fg='white', command=adminLoginScreen)
    login.grid(row=12, column=0)


def adminRegisterQuery():
    global password
    global username

    fname = fullname.get()
    usr = username.get()
    psw = password.get()
    print(fname)
    print(usr)
    print(psw)

    if len(usr) == 0:
        messagebox.showerror("Error", "Fields cannot be empty")
    else:
        try:
            # create a databases or connect to one
            conn = sqlite3.connect('db/admin.db')

            # create cursor
            c = conn.cursor()

            # Insert into table
            c.execute("INSERT INTO admin(full_name,username,password,role) VALUES (:full_name, :username, :password,:role )", {
                'full_name': fname,
                'username': usr,
                'password': psw,
                'role': 1

            })

            # showinfo messagebox
            print("Admin Registered Successfully")
            messagebox.showinfo("Customer account creation",
                                "Customer account created successfully")

            adminLoginScreen()
            adminRegister.destroy()

            conn.commit()
            conn.close()

        except sqlite3.Error as error:
            print("Error", "Something went wrong")


# ================================================================================================
# ============================= End Admin Register Screen | Query ================================
# ================================================================================================


# ================================================================================================
# ===================================  Welcome Screen ============================================
# ================================================================================================
title_text = Label(root, fg='white', text="WELCOME TO THE BANK",
                   font=("Arial", 30, "bold italic"), bg="#4A50E9")
title_text.grid(row=0, column=9, ipady=10, ipadx=10)

# frame 2
frame1 = Frame(root, bg="#0096FF", height=600, width=400)
frame1.grid(row=1, column=4, rowspan=4, columnspan=4, pady=70, padx=40)

# frame 3
frame2 = Frame(root, bg="white", height=600, width=800)
frame2.grid(row=1, column=8, rowspan=4, columnspan=4, pady=70, padx=40)

# Welcome SideBar Image
img = Image.open("bank.jpg")
img = img.resize((990, 600))  # resizing image
bank_img = ImageTk.PhotoImage(img)
label_img = Label(frame2, image=bank_img).grid(row=0, column=0)


# Admin Welcome Button
admin_button = Button(frame1, text="Admin", bg="#72FFFF", fg="black", font=(
    "Code New Roman", 10, "bold"), height=10, width=20, command=adminLoginScreen)
admin_button.grid(row=0, column=1, padx=100, pady=74)

# Customer Welcome Button
login_button = Button(frame1, text="Customer", bg="#72FFFF", fg="black", font=(
    "Code New Roman", 10, "bold"), height=10, width=20, command=customerLoginScreen)
login_button.grid(row=1, column=1, pady=65)


root.mainloop()

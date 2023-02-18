from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3
root = Tk()
root.geometry("1944x1080")
root["background"] = "#5800FF"
root.title("Bank Management System")

# ================================================================================================
# ============================== CREATING DATABASE FOR BANK APP ==================================
# ================================================================================================


# =========================== CREATING TABLE FOR AUTHENTICATION ==================================

# try:
#     # Giving database name
#     main_database = sqlite3.connect('bank.db')

#     # Initializing cursor
#     c = main_database.cursor()

#     # Creating customer table
#     c.execute("""CREATE TABLE authentication(
#                 full_name text,
#                 father_name text,
#                 gender text,
#                 email varchar,
#                 contact varchar,
#                 username text type UNIQUE NOT NULL,
#                 password varchar NOT NULL,
#                 account_type varchar,
#                 role integer
#                 )
#                 """)
#     print('Table created for authentication.')

#     # Committing and closing the database.
#     main_database.commit()
#     main_database.close()

# except sqlite3.Error as error:
#         print("Could not create table authentication.")


#=============================================================================================
#   =========================== END CREATING TABLE FOR AUTHENTICATION ========================
#=============================================================================================


    # def submit():
    #     #create a databases or connect to one
    #     conn=sqlite3.connect('customer_book.db')

    #     #create cursor
    #     c=conn.cursor()
        
    #     #Insert into table
    #     c.execute("INSERT INTO customer_register VALUES (:full_name, :father_name, :gender, :account_no, :contact, :account_type, :username, :password)",{
    #         'full_name':user.get(),
    #         'father_name':user1.get(),
    #         'gender':code.get(),
    #         'account_no':code1.get(),
    #         'contact':code2.get(),
    #         'account_type':confirm.get(),
    #         'username':user2.get(),
    #         'password':user3.get()

    #     })

    #     #showinfo messagebox
    #     messagebox.showinfo("Sign up", "Sigh Up Sucessful")

    #     conn.commit()
    #     conn.close()



def opening_customer_account():
    root=Toplevel()
    root.title("CUSTOMER REGISTER - BANKING APP")
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
            user.insert(0,'Enter Full Name')


    user=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user.grid(row=1,column=0, pady=10, ipadx=5)
    user.insert(0,'Enter Full Name')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)


    #Last name
    def on_enter(e):
        user1.delete(0,'end')

    def on_leave(e):
        name=user1.get()
        if name=='':
            user1.insert(0,"Father's Name")

    user1=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user1.grid(row=2,column=0 ,pady=10, ipadx=5)
    user1.insert(0,"Father's Name")
    user1.bind('<FocusIn>', on_enter)
    user1.bind('<FocusOut>', on_leave)


    #father's name
    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
        name=code.get()
        if name=="":
            code.insert(0,"Gender")

    code= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    code.grid(row=3,column=0, pady=10, ipadx=5)
    code.insert(0,"Gender")
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    #gender
    def on_enter(e):
        code1.delete(0,'end')

    def on_leave(e):
        name=code1.get()
        if name=='':
            code1.insert(0,'Account No')

    code1= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    code1.grid(row=4,column=0, pady=10, ipadx=5)
    code1.insert(0,'Account No')
    code1.bind('<FocusIn>', on_enter)
    code1.bind('<FocusOut>', on_leave)


    #email
    def on_enter(e):
        code2.delete(0,'end')

    def on_leave(e):
        name=code2.get()
        if name=='':
            code2.insert(0,'Mobile Number')

    code2= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    code2.grid(row=6,column=0, pady=10, ipadx=5)
    code2.insert(0,'Mobile Number')
    code2.bind('<FocusIn>', on_enter)
    code2.bind('<FocusOut>', on_leave)



    #account type
    confirm= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    confirm.grid(row=7,column=0, pady=10, ipadx=5)
    confirm.insert(0,'Savings Account')
    confirm.config(state= "disabled")

    # def disable_entry():

    #Username Entry
    def on_enter(e):
        user2.delete(0, 'end')

    def on_leave(e):
        name=user2.get()
        if name=='':
            user2.insert(0,'Enter a Username')


    user2=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user2.grid(row=8,column=0, pady=10, ipadx=5)
    user2.insert(0,'Enter a Username')
    user2.bind('<FocusIn>', on_enter)
    user2.bind('<FocusOut>', on_leave)


    #Password entry 
    def on_enter(e):
        user3.delete(0, 'end')

    def on_leave(e):
        name=user3.get()
        if name=='':
            user3.insert(0,'Enter Password')


    user3=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user3.grid(row=9,column=0, pady=10, ipadx=5)
    user3.insert(0,'Enter Password')
    user3.bind('<FocusIn>', on_enter)
    user3.bind('<FocusOut>', on_leave)


    #button for sign in
    signin= Button(frame, width=20,background='#3cdfff', text='Sign In',border=0, bg='#3cdfff', cursor='hand2', fg='white')
    signin.grid(row=11,column=0)

    # #label for already have an account?
    # acc=Label(frame,text="Already have an account? ", fg='#2c3e4c', bg='white', font=('Microsoft YaHei UI Light', 9))
    # acc.grid(row=12,column=0)

    # #button for login
    # login= Button(frame, width=15, text='Log In',border=0, bg='#3cdfff', cursor='hand2', fg='white')
    # login.grid(row=13,column=0)


    # conn.commit()
    # conn.close()
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
            user.insert(0,'Enter Full Name')


    user=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user.grid(row=1,column=0, pady=10, ipadx=5)
    user.insert(0,'Enter Full Name')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)


    #Last name
    def on_enter(e):
        user1.delete(0,'end')

    def on_leave(e):
        name=user1.get()
        if name=='':
            user1.insert(0,"Father's Name")

    user1=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user1.grid(row=2,column=0 ,pady=10, ipadx=5)
    user1.insert(0,"Father's Name")
    user1.bind('<FocusIn>', on_enter)
    user1.bind('<FocusOut>', on_leave)


    #father's name
    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
        name=code.get()
        if name=="":
            code.insert(0,"Gender")

    code= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    code.grid(row=3,column=0, pady=10, ipadx=5)
    code.insert(0,"Gender")
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    #gender
    def on_enter(e):
        code1.delete(0,'end')

    def on_leave(e):
        name=code1.get()
        if name=='':
            code1.insert(0,'Account No')

    code1= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    code1.grid(row=4,column=0, pady=10, ipadx=5)
    code1.insert(0,'Account No')
    code1.bind('<FocusIn>', on_enter)
    code1.bind('<FocusOut>', on_leave)


    #email
    def on_enter(e):
        code2.delete(0,'end')

    def on_leave(e):
        name=code2.get()
        if name=='':
            code2.insert(0,'Mobile Number')

    code2= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    code2.grid(row=6,column=0, pady=10, ipadx=5)
    code2.insert(0,'Mobile Number')
    code2.bind('<FocusIn>', on_enter)
    code2.bind('<FocusOut>', on_leave)



    #account type
    confirm= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    confirm.grid(row=7,column=0, pady=10, ipadx=5)
    confirm.insert(0,'Savings Account')
    confirm.config(state= "disabled")

    # def disable_entry():

    #Username Entry
    def on_enter(e):
        user2.delete(0, 'end')

    def on_leave(e):
        name=user2.get()
        if name=='':
            user2.insert(0,'Enter a Username')


    user2=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user2.grid(row=8,column=0, pady=10, ipadx=5)
    user2.insert(0,'Enter a Username')
    user2.bind('<FocusIn>', on_enter)
    user2.bind('<FocusOut>', on_leave)


    #Password entry 
    def on_enter(e):
        user3.delete(0, 'end')

    def on_leave(e):
        name=user3.get()
        if name=='':
            user3.insert(0,'Enter Password')


    user3=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user3.grid(row=9,column=0, pady=10, ipadx=5)
    user3.insert(0,'Enter Password')
    user3.bind('<FocusIn>', on_enter)
    user3.bind('<FocusOut>', on_leave)


    # #button for sign in
    # signin= Button(frame, width=20,background='#3cdfff', text='Sign In',border=0, bg='#3cdfff', cursor='hand2', fg='white')
    # signin.grid(row=11,column=0)

    # #label for already have an account?
    # acc=Label(frame,text="Already have an account? ", fg='#2c3e4c', bg='white', font=('Microsoft YaHei UI Light', 9))
    # acc.grid(row=12,column=0)

    #button for login
    login= Button(frame, width=15, text='Log In',border=0, bg='#3cdfff', cursor='hand2', fg='white')
    login.grid(row=13,column=0)


    # conn.commit()
    # conn.close()

#=============================================================================================
# =======================END OF CREATING REGISTRATION FORM FOR CUSTOMER=======================
#=============================================================================================


def withdraw():
    global label_img
    root=Toplevel()
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

    Withdraw_btn=Button(root,text="Withdraw", fg="white", bg="blue2",font=("Verdana Bold", 14))
    Withdraw_btn.grid(row=10,column=1)

#   =========================== END OF WITHDRAW ========================
def customerDashboard():
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

    customer_img1 = Image.open("customer_image.jpg")
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

    amount_to_deposit=Entry(root,width=30)
    amount_to_deposit.grid(row=3,column=1)

    name_label=Label(root,text="Name")
    name_label.grid(row=1,column=0)

    account_num_label=Label(root,text="Account Number")
    account_num_label.grid(row=2,column=0)

    amount_to_deposit_label=Label(root,text="Amount to deposit")
    amount_to_deposit_label.grid(row=3,column=0)

    Deposit_btn=Button(root,text="Deposit", fg="white", bg="blue2",font=("Verdana Bold", 14))
    Deposit_btn.grid(row=4,column=1)


def balance_enquiry():
    balance_enquiry = Toplevel()
    balance_enquiry.title("Balance Enquiry")
    balance_enquiry.geometry("700x200")
    balance_enquiry["background"] = "pink"
    balance_enquiry_label = Label(balance_enquiry,text="Your current balance is Rs. .......",font=("Code New Roman",24,"bold"),bg="pink")
    balance_enquiry_label.grid(row=3,column=2,pady=70,padx=20)
    balance_enquiry_button = Button(customer_features_frame,text="Balance Enquiry",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24,command=balance_enquiry)
    balance_enquiry_button.grid(row=2,column=0,pady=2)


# ================================================================================================
# ============================== Customer Login Screen | Query ===================================
# ================================================================================================

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
            user.delete(0, 'end')

    def on_leave(e):
            name = user.get()
            if name == '':
                user.insert(0, 'Username')

    username = Entry(frame, width=25, fg="black", border=1,
                    bg='white', font=('Microsoft YaHei UI Light', 11))
    username.grid(row=2, column=0, pady=10, ipadx=5, ipady=5, padx=1)
    username.bind('<FocusIn>', on_enter)
    username.bind('<FocusOut>', on_leave)

        # entry for password
    def on_enter(e):
            code.delete(0, 'end')

    def on_leave(e):
            global code
            name = code.get()
            if name == '':
                code.insert(0, 'Password')

    password = Entry(frame, width=25, fg='black', border=1,
                    bg='white', font=('Microsoft YaHei UI Light', 11))
    password.grid(row=3, column=0, pady=10, ipadx=5, ipady=5)
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)

        # login button
    btn = Button(frame, width=25, pady=7, text='Log In',
                    bg='#57a1f8', fg='white', border=0, command=customerLoginQuery)
    btn.grid(row=4, column=0)

    #     # text
    # label = Label(frame, text="Don't have an account? ", fg='black',
    #                 bg='white', font=('Microsoft YaHei UI Light', 9))
    # label.grid(row=5, column=0)

    #     # sign up button
    # sign_up = Button(frame, width=20, pady=7, text='Sign Up', border=0,
    #                     bg='#57a1f8', cursor='hand2', fg='white', command=customerRegisterScreen)
    # sign_up.grid(row=6, column=0)



def customerLoginQuery():
    user = username.get()
    psw = password.get()
    role=1

    if len(user) == 0 or len(psw) == 0:
        messagebox.showinfo("Warning", "Fields cannot be empty")
    else:
        try:
            main_database = sqlite3.connect('bank.db')
            c = main_database.cursor()
                
            c.execute("SELECT * FROM authentication WHERE username = ? AND password = ? AND role = ? ",(user,psw,role))
            data = c.fetchone()

            if data:
                    # messagebox.showinfo("Success", " Login success")
                    # Call Dashboard Function Here
                    customerDashboard()

            else:
                messagebox.showerror("Error", "No user found")
                    
            main_database.commit()
            main_database.close()

        except sqlite3.Error as error:
            print("Could not login to the system")


# ================================================================================================
# ===================== End Customer Login Screen | Query ========================================
# ================================================================================================




# ================================================================================================
# ===============================Customer Register Screen | Query ================================
# ================================================================================================
def customerRegisterQuery():
    username = user2.get()
    global password
    password = user3.get()
    print(username)

    if len(username) == 0 :
        messagebox.showerror("Error", "Fields cannot be empty")
    else:
        try:
            #create a databases or connect to one
            conn=sqlite3.connect('bank.db')

            #create cursor
            c=conn.cursor()
            
            #Insert into table
            c.execute("INSERT INTO authentication(full_name,father_name,gender,email,contact,username,password,role) VALUES (:full_name, :father_name, :gender, :email, :contact,  :username, :password)",{
                'full_name':user.get(),
                'father_name':code.get(),
                'gender':code1.get(),
                'email':code2.get(),
                'contact':confirm.get(),
                'username':user2.get(),
                'password':user3.get(),


            })

            #showinfo messagebox
            print("Customer Registered Successfully")
            messagebox.showinfo("Sign up", "Sigh Up Sucessful")

            conn.commit()
            conn.close()
            
        except sqlite3.Error as error:
                print("Could not create table authentication.")


def customerRegisterScreen():
    global user
    global user2
    global user3
    global code
    global code1
    global code2
    global confirm
    global confirm1

    customerRegister=Toplevel()
    customerRegister.title('CUSTOMER REGISTER - BANKING APP')
    customerRegister.geometry('925x500+300+200')
    customerRegister.configure(bg='#fff')

    #mainframe
    mainframe= Frame(customerRegister, bg="#fff")
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

    #full name
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Full Name')


    user=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user.grid(row=1,column=0, pady=10, ipadx=5)
    user.insert(0,'Full Name')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)


    #father's name
    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
        name=code.get()
        if name=="":
            code.insert(0,"Father's Name")

    code= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    code.grid(row=2,column=0, pady=10, ipadx=5)
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
    code1.grid(row=3,column=0, pady=10, ipadx=5)
    code1.insert(0,'Gender')
    code1.bind('<FocusIn>', on_enter)
    code1.bind('<FocusOut>', on_leave)


    #email
    def on_enter(e):
        code2.delete(0,'end')

    def on_leave(e):
        name=code2.get()
        if name=='':
            code2.insert(0,'Email')

    code2= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    code2.grid(row=4,column=0, pady=10, ipadx=5)
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
    confirm.grid(row=5,column=0, pady=10, ipadx=5)
    confirm.insert(0,'Mobile Number')
    confirm.bind('<FocusIn>', on_enter)
    confirm.bind('<FocusOut>', on_leave)


    #first name
    def on_enter(e):
        user2.delete(0, 'end')

    def on_leave(e):
        name=user2.get()
        if name=='':
            user2.insert(0,'Enter a Username')


    user2=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user2.grid(row=6,column=0, pady=10, ipadx=5)
    # user2.insert(0,'Enter a Username')
    user2.bind('<FocusIn>', on_enter)
    user2.bind('<FocusOut>', on_leave)

    #first name
    def on_enter(e):
        user3.delete(0, 'end')

    def on_leave(e):
        name=user3.get()
        if name=='':
            user3.insert(0,'Enter Password')


    user3=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user3.grid(row=7,column=0, pady=10, ipadx=5)
    user3.bind('<FocusIn>', on_enter)
    user3.bind('<FocusOut>', on_leave)

    ####
    confirm1= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    confirm1.grid(row=8,column=0, pady=10, ipadx=5)
    confirm1.insert(0,'1')
    confirm1.config(state= "disabled")

    #button for login
    login= Button(frame, width=15, text='Log In',border=0, bg='#3cdfff', cursor='hand2', fg='white', command=customerLoginScreen)
    login.grid(row=12,column=0)

    customerRegister.mainloop()
    # customerRegister.destroy()
    # customerLoginScreen



    
def adminDashboard():
    global admin_img_label
    admin_page = Toplevel()
    admin_page.geometry("1100x750")
    admin_page["background"] = "#86E5FF"
    admin_features_frame = Frame(admin_page,bg="#86E5FF",height=750,width=400)
    admin_features_frame.grid(row=0,column=0,padx=20,pady=20)
    open_acc_button = Button(admin_features_frame,text="Opening Account",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24, command=opening_customer_account)
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
    admin_img_label = Label(admin_image_frame,image=admin_img).grid(row=0,column=8,padx=50)

    admin_page.mainloop()



# ================================================================================================
# ============================= End  Customer Register Screen | Query ============================
# ================================================================================================

# ================================================================================================
# ============================== Admin Login Screen | Query ======================================
# ================================================================================================

def adminLoginScreen():
    adminLogin = Toplevel()
    adminLogin.title('ADMIN LOGIN SCREEN - BANK APP')
    adminLogin.geometry('925x500+300+200')
    adminLogin.configure(bg='#fff')

    global username
    global password


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
        role=1

        if len(user) == 0 or len(psw) == 0:
            messagebox.showinfo("Warning", "Fields cannot be empty")
        else:
            try:
                main_database = sqlite3.connect('bank.db')
                c = main_database.cursor()
                
                c.execute("SELECT * FROM authentication WHERE username = ? AND password = ? AND role = ? ",(user,psw,role))
                data = c.fetchone()

                if data:
                        # messagebox.showinfo("Success", " Login success")
                        # Call Dashboard Function Here 
                        adminDashboard()
                        

                else:
                    messagebox.showerror("Error", "No user found")
                    
                main_database.commit()
                main_database.close()

            except sqlite3.Error as error:
                print("Could not login to the system")


# ================================================================================================
# ============================== End Admin Login Screen | Query ==================================
# ================================================================================================

# ================================================================================================
# ============================== Admin Registration Screen | Query ===============================
# ================================================================================================


def adminRegisterScreen():
    global user
    global user2
    global user3
    global code
    global code1
    global code2
    global confirm
    global confirm1

    adminRegister=Toplevel()
    adminRegister.title('ADMIN REGISTER - BANKING APP')
    adminRegister.geometry('925x500+300+200')
    adminRegister.configure(bg='#fff')

    #mainframe
    mainframe= Frame(adminRegister, bg="#fff")
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

    #full name
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='Full Name':
            user.insert(0,'Full Name')


    user=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user.grid(row=1,column=0, pady=10, ipadx=5)
    user.insert(0,'Full Name')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)


    #father's name
    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
        name=code.get()
        if name=="Father's Name":
            code.insert(0,"Father's Name")

    code= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    code.grid(row=2,column=0, pady=10, ipadx=5)
    code.insert(0,"Father's Name")
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    #gender
    def on_enter(e):
        code1.delete(0,'end')

    def on_leave(e):
        name=code1.get()
        if name=='Gender':
            code1.insert(0,'Gender')

    code1= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    code1.grid(row=3,column=0, pady=10, ipadx=5)
    code1.insert(0,'Gender')
    code1.bind('<FocusIn>', on_enter)
    code1.bind('<FocusOut>', on_leave)


    #email
    def on_enter(e):
        code2.delete(0,'end')

    def on_leave(e):
        name=code2.get()
        if name=='Email':
            code2.insert(0,'Email')

    code2= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    code2.grid(row=4,column=0, pady=10, ipadx=5)
    code2.insert(0,'Email')
    code2.bind('<FocusIn>', on_enter)
    code2.bind('<FocusOut>', on_leave)


    #mobile number
    def on_enter(e):
        confirm.delete(0,'end')

    def on_leave(e):
        name=confirm.get()
        if name=='Mobile Number':
            confirm.insert(0,'Mobile Number')

    confirm= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    confirm.grid(row=5,column=0, pady=10, ipadx=5)
    confirm.insert(0,'Mobile Number')
    confirm.bind('<FocusIn>', on_enter)
    confirm.bind('<FocusOut>', on_leave)


    #first name
    def on_enter(e):
        user2.delete(0, 'end')

    def on_leave(e):
        name=user2.get()
        if name=='':
            user2.insert(0,'Enter a Username')


    user2=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user2.grid(row=6,column=0, pady=10, ipadx=5)
    # user2.insert(0,'Enter a Username')
    user2.bind('<FocusIn>', on_enter)
    user2.bind('<FocusOut>', on_leave)

    #first name
    def on_enter(e):
        user3.delete(0, 'end')

    def on_leave(e):
        name=user3.get()
        if name=='':
            user3.insert(0,'Enter Password')


    user3=Entry(frame,width=25, fg="black", border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
    user3.grid(row=7,column=0, pady=10, ipadx=5)
    user3.bind('<FocusIn>', on_enter)
    user3.bind('<FocusOut>', on_leave)

    ####
    confirm1= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
    confirm1.grid(row=8,column=0, pady=10, ipadx=5)
    confirm1.insert(0,'1')
    confirm1.config(state= "disabled")


    #button for sign in
    signin= Button(frame, width=20,background='#3cdfff', text='Sign In',border=0, bg='#3cdfff', cursor='hand2', fg='white', command=adminRegisterQuery)
    signin.grid(row=10,column=0)

    #label for already have an account?
    acc=Label(frame,text="Already have an account? ", fg='#2c3e4c', bg='white', font=('Microsoft YaHei UI Light', 9))
    acc.grid(row=11,column=0)

    #button for login
    login= Button(frame, width=15, text='Log In',border=0, bg='#3cdfff', cursor='hand2', fg='white', command=adminLoginScreen)
    login.grid(row=12,column=0)

    # adminRegister.mainloop()
    # adminRegister.destroy()
    # adminLoginScreen


def adminRegisterQuery():
    global password
    username = user2.get()
    password = user3.get()
    print(username)

    if len(username) == 0 :
        messagebox.showerror("Error", "Fields cannot be empty")
    else:
        try:
            #create a databases or connect to one
            conn=sqlite3.connect('bank.db')

            #create cursor
            c=conn.cursor()
            
            #Insert into table
            c.execute("INSERT INTO authentication(full_name,father_name,gender,email,contact,username,password,role) VALUES (:full_name, :father_name, :gender, :email, :contact,  :username, :password,:role )",{
                'full_name':user.get(),
                'father_name':code.get(),
                'gender':code1.get(),
                'email':code2.get(),
                'contact':confirm.get(),
                'username':user2.get(),
                'password':user3.get(),
                'role': 1

            })

            #showinfo messagebox
            print("Admin Registered Successfully")
            messagebox.showinfo("Sign up", "Sigh Up Sucessful")

            conn.commit()
            conn.close()
            
        except sqlite3.Error as error:
                print("Could not create table authentication.")




# ================================================================================================
# ============================= End Admin Register Screen | Query ================================
# ================================================================================================




# ================================================================================================
# ===================================  Welcome Screen ============================================
# ================================================================================================


title_text = Label(root,fg='#fff',text="WELCOME TO THE BANK",font=("Arial",24,"bold italic"),bg="#5800FF")
title_text.grid(row=0,column=9, ipady=10, ipadx=10)

#frame 2
frame1 = Frame(root,bg="#0096FF",height=600,width=400)
frame1.grid(row=1,column=4,rowspan=4,columnspan=4,pady=70,padx=40)

#frame 3
frame2 = Frame(root,bg="white",height=600,width=800)
frame2.grid(row=1,column=8,rowspan=4,columnspan=4,pady=70,padx=40)

# Welcome SideBar Image 
img = Image.open("bank.jpg")
img = img.resize((990,600))     #resizing image
bank_img = ImageTk.PhotoImage(img)
label_img = Label(frame2,image=bank_img).grid(row=0,column=0)


# Admin Welcome Button
admin_button = Button(frame1,text="Admin",bg="#72FFFF",fg="black",font = ("Code New Roman",10,"bold"),height=10,width=20,command=adminLoginScreen)
admin_button.grid(row=0,column=1,padx=100,pady=74)

# Customer Welcome Button
login_button = Button(frame1,text="Customer",bg="#72FFFF",fg="black",font= ("Code New Roman",10,"bold"),height=10,width=20,command=customerLoginScreen)
login_button.grid(row=1,column=1,pady=65)


root.mainloop()

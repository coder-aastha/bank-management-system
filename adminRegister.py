from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.title('REGISTER')
root.geometry('925x500+300+200')
root.configure(bg='#fff')


#   =========================== CREATING DB TABLE ========================

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
#                 username text type UNIQUE,
#                 password varchar,
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


def registerAdmin():
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
    # messagebox.showinfo("Sign up", "Sigh Up Sucessful")
    print("Admin Registered Successfully")

    conn.commit()
    conn.close()



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
user2.insert(0,'Enter a Username')
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
user3.insert(0,'Enter Password')
user3.bind('<FocusIn>', on_enter)
user3.bind('<FocusOut>', on_leave)

####
confirm1= Entry(frame,width=25, fg='black', border=1, bg= 'white', font=('Microsoft YaHei UI Light', 11))
# confirm1.grid(row=8,column=0, pady=10, ipadx=5)
confirm1.insert(0,'1')
confirm1.config(state= "disabled")


#button for sign in
signin= Button(frame, width=20,background='#3cdfff', text='Sign In',border=0, bg='#3cdfff', cursor='hand2', fg='white', command=registerAdmin)
signin.grid(row=10,column=0)

#label for already have an account?
acc=Label(frame,text="Already have an account? ", fg='#2c3e4c', bg='white', font=('Microsoft YaHei UI Light', 9))
acc.grid(row=11,column=0)

#button for login
login= Button(frame, width=15, text='Log In',border=0, bg='#3cdfff', cursor='hand2', fg='white')
login.grid(row=12,column=0)



root.mainloop()
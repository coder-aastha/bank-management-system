# login page
from tkinter import *
from tkinter import messagebox
import sqlite3


root = Tk()
root.title('LOGIN')
root.geometry('925x500+300+200')
root.configure(bg='#fff')

def login():
    global username
    global password

    main_database = sqlite3.connect('bank.db')
    c = main_database.cursor()
    
    username = user.get()
    password = code.get()
    role = 1

    c.execute("SELECT * FROM authentication WHERE username = ? AND password = ? AND role = ? ",(username,password,role))
    data = c.fetchone()

    if data:
            messagebox.showinfo("Success", " Login success")
            # Call Dashboard Function Here 
    else:
          messagebox.showerror("Error", "No user found")
         
    main_database.commit()
    main_database.close()
 
mainframe = Frame(root, bg='#fff')
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

user = Entry(frame, width=25, fg="black", border=1,
                 bg='white', font=('Microsoft YaHei UI Light', 11))
user.grid(row=2, column=0, pady=10, ipadx=5, ipady=5, padx=1)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

    # entry for password
def on_enter(e):
        code.delete(0, 'end')

def on_leave(e):
        name = code.get()
        if name == '':
            code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=1,
                 bg='white', font=('Microsoft YaHei UI Light', 11))
code.grid(row=3, column=0, pady=10, ipadx=5, ipady=5)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

    # login button
btn = Button(frame, width=25, pady=7, text='Log In',
                 bg='#57a1f8', fg='white', border=0, command=login)
btn.grid(row=4, column=0)

    # text
label = Label(frame, text="Don't have an account? ", fg='black',
                  bg='white', font=('Microsoft YaHei UI Light', 9))
label.grid(row=5, column=0)

    # sign up button
sign_up = Button(frame, width=20, pady=7, text='Sign Up', border=0,
                     bg='#57a1f8', cursor='hand2', fg='white')
sign_up.grid(row=6, column=0)




root.mainloop()

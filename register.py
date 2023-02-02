from tkinter import *

window=Tk()
window.title('REGISTER')
window.geometry('925x500+300+200')
window.configure(bg='#fff')

#mainframe
mainframe= Frame(window, bg="#fff")
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
login= Button(frame, width=15, text='Log In',border=0, bg='#3cdfff', cursor='hand2', fg='white')
login.grid(row=13,column=0)

window.mainloop()
from tkinter import*
import sqlite3
root= Tk()
root.geometry("800x450")
root.resizable(False,False)
root["background"] = "skyblue"
root.title("Update")
f = ('Times', 14)

frame = Frame(root,bd=2,bg='lightpink',relief=SOLID, padx=25,pady=10)
frame.grid(row=1, column=1,padx=300,pady=40,ipadx=20,ipady=30)

Label(frame,text="User ID",bg='grey',font=f).grid(row=0, column=0, sticky=W, pady=10)
Label(frame,text="Password ",bg='grey',font=f).grid(row=1, column=0, sticky=W, pady=10)
Update_btn = Button(frame, width=15,  text='UPDATE', bg='grey', font=f, relief=SOLID,cursor='hand2',command=None)
User_ID = Entry(frame, font=f)
Password_ID = Entry(frame, font=f)

User_ID.grid(row=0, column=1, pady=10, padx=20)
Password_ID.grid(row=1, column=1, pady=10, padx=20)
Update_btn.grid(row=2, column=1, pady=10, padx=20)

frame.grid()


root.mainloop()

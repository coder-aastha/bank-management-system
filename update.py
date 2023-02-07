from tkinter import*
ws = Tk()
ws.geometry("800x450")
ws.resizable(False,False)
ws["background"] = "skyblue"
ws.title("Update")
f = ('Times', 14)

frame = Frame(ws,bd=2,bg='lightpink',relief=SOLID, padx=35,pady=15)
frame.grid(row=1, column=1,padx=400,pady=50,ipadx=20,ipady=30)

Label(frame,text="Enter ID",bg='grey',font=f).grid(row=0, column=0, sticky=W, pady=10)

Update_btn = Button(frame, width=15,  text='UPDATE', bg='grey', font=f, relief=SOLID,cursor='hand2',command=None)

register_ID = Entry(frame, font=f)
register_Upload = Entry(frame, font=f)

register_ID.grid(row=0, column=1, pady=10, padx=20)
Update_btn.grid(row=1, column=1, pady=10, padx=20)

frame.grid()

ws.mainloop()

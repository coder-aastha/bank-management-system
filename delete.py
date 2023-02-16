from tkinter import*
import sqlite3
ws = Tk()
ws.geometry("800x450")
ws.resizable(False,False)
ws["background"] = "skyblue"
ws.title("DELETE")
f = ('Times', 14)

frame = Frame(ws,bd=2,bg='lightpink',relief=SOLID, padx=35,pady=15)
frame.grid(row=1, column=1,padx=400,pady=50,ipadx=20,ipady=30)

Label(frame,text="Enter ID",bg='grey',font=f).grid(row=0, column=0, sticky=W, pady=10)

Delete_btn = Button(frame, width=15,  text='DELETE', bg='grey', font=f, relief=SOLID,cursor='hand2',command=None)

register_ID = Entry(frame, font=f)
register_Delete = Entry(frame, font=f)

register_ID.grid(row=0, column=1, pady=10, padx=20)
Delete_btn.grid(row=1, column=1, pady=10, padx=20)
frame.grid()


#   =========================== CREATING DB TABLE ========================#
try:

    #  Giving .database. name#     
     main_database = sqlite3.connect('bank.db')
     c = main_database.cursor()

    #  Creating.Delete. table    
     c.execute("""CREATE TABLE DELETE(
      ID INTEGER) """)
      
     print('Table created for DELETE.')
    #  Committing and closing the database. 
     main_database.commit()
     main_database.close()
except sqlite3.Error as error:
    print("Could not create DB customer")


ws.mainloop()


from tkinter import *
import tkinter as Toplevel
import sqlite3

# Create a Tkinter window
root = Tk()
root.title("Balance Enquiry")
root.geometry("700x200")
root["background"] = "#86E5FF"
balance_enquriy_label = Label(root,text="Your current balance is Rs. .......",font=("Code New Roman",24,"bold"),bg="#86E5FF")
balance_enquriy_label.grid(row=3,column=2,pady=70,padx=20)

# # Create a database connection
conn = sqlite3.connect('bank.db')

#   =========================== CREATING DB TABLE ========================#
try:

    #  Giving .database. name#     
     main_database = sqlite3.connect('bank.db')
     c = main_database.cursor()

    #  Creating.Delete(
    #       ID INTEGER) """)
          
     print('Table created for balance_enquiry')
    
except sqlite3.Error as error:
    print("Could not create DB balance_enquiry")



# Start the Tkinter event loop
root.mainloop()
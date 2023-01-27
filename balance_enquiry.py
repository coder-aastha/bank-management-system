from tkinter import *
import os  #To represent how many files are there
balance_enquriy = Tk()
balance_enquriy.title("Balance Enquiry")
balance_enquriy.geometry("700x200")
balance_enquriy["background"] = "#86E5FF"
balance_enquriy_label = Label(balance_enquriy,text="Your current balance is Rs. .......",font=("Code New Roman",24,"bold"),bg="#86E5FF")
balance_enquriy_label.grid(row=3,column=2,pady=70,padx=20)
balance_enquriy.mainloop()
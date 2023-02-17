
from tkinter import *
from PIL import Image,ImageTk

customer_page = Tk()
customer_page.geometry("1100x740")
customer_page["background"] = "#86E5FF"

customer_features_frame = Frame(customer_page,bg="#86E5FF",height=750,width=400)
customer_features_frame.grid(row=0,column=0,padx=20,pady=20)

deposit_button = Button(customer_features_frame,text="Deposit",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24)
deposit_button.grid(row=0,column=0)

withdraw_button = Button(customer_features_frame,text="Withdraw",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24)
withdraw_button.grid(row=1,column=0,pady=20)

balance_enquiry_button = Button(customer_features_frame,text="Balance enquiry",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24)
balance_enquiry_button.grid(row=2,column=0,pady=1)
def balance_enquiry():
    balance_enquiry = Toplevel()
    balance_enquiry.title("Balance Enquiry")
    balance_enquiry.geometry("700x200")
    balance_enquiry["background"] = "pink"
    balance_enquiry_label = Label(balance_enquiry,text="Your current balance is Rs. .......",font=("Code New Roman",24,"bold"),bg="pink")
    balance_enquiry_label.grid(row=3,column=2,pady=70,padx=20)
balance_enquiry_button = Button(customer_features_frame,text="Balance Enquiry",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24,command=balance_enquiry)
balance_enquiry_button.grid(row=2,column=0,pady=2)


customer_image_frame = Frame(customer_page,bg="#86E5FF",height=700,width=600)
customer_image_frame.grid(row=0,column=5,padx=10,pady=0)

customer_img1 = Image.open("customer_image.jpg")
customer_img1 = customer_img1.resize((720,700))     #resizing image
customer_img = ImageTk.PhotoImage(customer_img1)
label_customer_img = Label(customer_image_frame,image=customer_img).grid(row=0,column=8,padx=50)

customer_page.mainloop()
from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.geometry("1944x1080")
root["background"] = "#5800FF"
root.title("Bank Management System")

def admin_page_open():
    admin_page = Toplevel()
    admin_page.geometry("1100x750")
    admin_page["background"] = "#86E5FF"
    admin_features_frame = Frame(admin_page,bg="#86E5FF",height=750,width=400)
    admin_features_frame.grid(row=0,column=0,padx=20,pady=20)
    open_acc_button = Button(admin_features_frame,text="Opening Account",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24)
    open_acc_button.grid(row=0,column=0)
    cus_details_button = Button(admin_features_frame,text="Showing Customer Details",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24)
    cus_details_button.grid(row=1,column=0,pady=20)
    closing_acc_button = Button(admin_features_frame,text="Closing Account",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24)
    closing_acc_button.grid(row=2,column=0,pady=2)

    admin_image_frame = Frame(admin_page,bg="#86E5FF",height=700,width=600)
    admin_image_frame.grid(row=0,column=5,padx=10,pady=0)

    img_of_admin = Image.open("image/admin_img.png")
    img_of_admin = img_of_admin.resize((720,700))     #resizing image
    admin_img = ImageTk.PhotoImage(img_of_admin)
    admin_img_label = Label(admin_image_frame,image=admin_img).grid(row=0,column=8,padx=50)

def login():
    login_page = Toplevel()
    login_page.title("Login")
    login_page.geometry("800x800")
    # login_page_frame = Frame(login_page,height=400,width=400,bg="yellow")
    # login_page_frame.grid(row=0,column=0)
    login_page_button = Button(login_page,text="Click Me",bg="black",fg="white",command=admin_page_open)
    login_page_button.grid(row=3,column=3)

#Making frames (frame 1)
# frame_welcome = Frame(root)
# frame_welcome.grid(row=0,column=0,pady=20)


def customer_page_open():
    global customer_page
    global customer_features_frame
    customer_page = Toplevel()
    customer_page.geometry("1100x740")
    customer_page["background"] = "#86E5FF"

    customer_features_frame = Frame(customer_page,bg="#86E5FF",height=750,width=400)
    customer_features_frame.grid(row=0,column=0,padx=20,pady=20)

    deposit_button = Button(customer_features_frame,text="Deposit",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24)
    deposit_button.grid(row=0,column=0)

    withdraw_button = Button(customer_features_frame,text="Withdraw",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24)
    withdraw_button.grid(row=1,column=0,pady=20)

    balance_enquiry_button = Button(customer_features_frame,text="Balance enquiry",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24,command=balance_enquiry)
    balance_enquiry_button.grid(row=2,column=0,pady=1)

    customer_image_frame = Frame(customer_page,bg="#86E5FF",height=700,width=600)
    customer_image_frame.grid(row=0,column=5,padx=10,pady=0)

    customer_img1 = Image.open("image/customer_image.jpg")
    customer_img1 = customer_img1.resize((720,700))     #resizing image
    customer_img = ImageTk.PhotoImage(customer_img1)
    label_customer_img = Label(customer_image_frame,image=customer_img).grid(row=0,column=8,padx=50)

def balance_enquiry():
    balance_enquiry = Toplevel()
    balance_enquiry.title("Balance Enquiry")
    balance_enquiry.geometry("700x200")
    balance_enquiry["background"] = "pink"
    balance_enquiry_label = Label(balance_enquiry,text="Your current balance is Rs. .......",font=("Code New Roman",24,"bold"),bg="pink")
    balance_enquiry_label.grid(row=3,column=2,pady=70,padx=20)
    balance_enquiry_button = Button(customer_features_frame,text="Balance Enquiry",bg="#5BC0F8",font=("Code New Roman",10,"bold"),height=13,width=24,command=balance_enquiry)
    balance_enquiry_button.grid(row=2,column=0,pady=2)


def customer_login():
        customer_login_page = Toplevel()
        customer_login_page.title("Login")
        customer_login_page.geometry("800x800")
        # login_page_frame = Frame(login_page,height=400,width=400,bg="yellow")
        # login_page_frame.grid(row=0,column=0)
        customer_login_page_button = Button(customer_login_page,text="Click Me",bg="black",fg="white",command=customer_page_open)
        customer_login_page_button.grid(row=4,column=6)


title_text = Label(root,text="WELCOME TO BANK",font=("Code New Roman",21,"bold"),bg="#00D7FF")
title_text.grid(row=0,column=9)

#frame 2
frame1 = Frame(root,bg="#0096FF",height=600,width=400)
frame1.grid(row=1,column=4,rowspan=4,columnspan=4,pady=70,padx=40)

#frame 3
frame2 = Frame(root,bg="white",height=600,width=800)
frame2.grid(row=1,column=8,rowspan=4,columnspan=4,pady=70,padx=40)

#adding image
#bank_image = ImageTk.PhotoImage(Image.open("Profile.png"))
img = Image.open("image/bank.jpg")
img = img.resize((990,600))     #resizing image
bank_img = ImageTk.PhotoImage(img)
label_img = Label(frame2,image=bank_img).grid(row=0,column=0)

#Creating buttons
admin_button = Button(frame1,text="Admin",bg="#72FFFF",fg="black",font = ("Code New Roman",10,"bold"),height=10,width=20,command=login)
admin_button.grid(row=0,column=1,padx=100,pady=74)
# admin_button.
login_button = Button(frame1,text="Customer",bg="#72FFFF",fg="black",font= ("Code New Roman",10,"bold"),height=10,width=20,command=customer_login)
login_button.grid(row=1,column=1,pady=65)


root.mainloop()
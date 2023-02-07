from tkinter import *
from PIL import Image,ImageTk

admin_page = Tk()
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

img1 = Image.open("admin_img.png")
img1 = img1.resize((720,700))     #resizing image
admin_img = ImageTk.PhotoImage(img1)
label_img_admin = Label(admin_image_frame,image=admin_img).grid(row=0,column=8,padx=50)

admin_page.mainloop()
import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(
    user='root',
    password='T@ekwondo12',
    host='localhost',
    database='bank_management'
)
cursor = cnx.cursor()
# if cnx.is_connected:
#     print("Success")
while True:
    account_number = int(input("Enter your account number\n"))
    balance = int(input("Enter your balance\n"))
    query = "Insert into accounts values({},{})".format(account_number,balance)
    cursor.execute(query)
    cnx.commit()
    print("Account created successfully")
    x = int(input("1. Enter more values\n 2. Exit\n"))
    if x == 2:
        break



    



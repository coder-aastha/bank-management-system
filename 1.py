import sqlite3
connection = sqlite3("update.py")

cursor= connection.cursor()
 #create update table

command="""CREATE TABLE IF NOT EXISTS update (Update INTEGER PRIMARY KEY , UPDATE TEXT)"""
cursor.execute(command)

cursor.execute("INSERT INTO ENTER ID (ram, shyam,hari)")
cursor.execute("select * FROM ENTER ID")
 
results= cursor.fetchall()
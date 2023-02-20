
import sqlite3

try:
    # Giving database name
    user_database = sqlite3.connect('db/user.db')

    # Initializing cursor
    c = user_database.cursor()

    # Creating customer table
    c.execute("""CREATE TABLE user(
                full_name text,
                father_name text,
                account_no varchar ,
                gender text,
                contact varchar,
                account_type varchar,
                balance integer,
                username text type UNIQUE NOT NULL,
                password varchar NOT NULL
                )
                """)
    print('Table created for user.')

    # Committing and closing the database.
    user_database.commit()
    user_database.close()

except sqlite3.Error as error:
        print(error)
        print("Could not create table for user.")


            

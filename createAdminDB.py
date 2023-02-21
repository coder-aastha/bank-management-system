
import sqlite3

try:
    # Giving database name
    main_database = sqlite3.connect('db/admin.db')

    # Initializing cursor
    c = main_database.cursor()

    print(c)

    # Creating customer table
    c.execute("""CREATE TABLE admin(
                full_name text,
                username text type UNIQUE NOT NULL,
                password varchar NOT NULL,
                role integer
                )
                """)
    print('Table created for admin.')

    # Committing and closing the database.
    main_database.commit()
    main_database.close()

except sqlite3.Error as error:
        print("Could not create table for admin.")


            


import sqlite3

try:
    # Giving database name
    main_database = sqlite3.connect('bank.db')

    # Initializing cursor
    c = main_database.cursor()

    print(c)

    # Creating customer table
    c.execute("""CREATE TABLE authentication(
                full_name text,
                father_name text,
                account_no varchar,
                gender text,
                contact varchar,
                username text type UNIQUE NOT NULL,
                password varchar NOT NULL,
                account_type varchar,
                balance integer,
                role integer
                )
                """)
    print('Table created for authentication.')

    # Committing and closing the database.
    main_database.commit()
    main_database.close()

except sqlite3.Error as error:
        print("Could not create table authentication.")


            

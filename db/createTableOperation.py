import sqlite3

def createTables():
    conn = sqlite3.connect("my_medicalshop.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        id int primary key,
        user_id varchar(100),
        password varchar(100),
        level int,
        date_of_account_creation date,
        isApproved boolean,
        block boolean,
        name varchar(255),
        email varchar(255),
        pin varchar(6),
        address varchar(255),
        phoneNo int    
    );
    """)

    conn.commit()
    conn.close()

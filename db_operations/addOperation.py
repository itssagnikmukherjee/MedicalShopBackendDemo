import sqlite3
import uuid
from datetime import date

def createUser(name,password,email,pinCode,address,phoneNo):
    conn = sqlite3.connect("databases/user_info.db")
    cursor = conn.cursor()

    user_id = str(uuid.uuid4())

    date_of_account_creation = date.today()

    cursor.execute(
    """
    INSERT INTO Users(user_id,password,level,date_of_account_creation,isApproved,block,name,email,pin,address,phoneNo)
    VALUES(?,?,?,?,?,?,?,?,?,?,?)
    """,(user_id,password,1,date_of_account_creation,0,0,name,email,pinCode,address,phoneNo)
    )

    conn.commit()
    conn.close()

    return {"message": "User created successfully", "user_id": user_id, "user_name": name}


def createNewProduct(product_name,stock,price,category,expiry_date):
    conn = sqlite3.connect("databases/products.db")
    cursor = conn.cursor()

    cursor.execute(
    """
    INSERT INTO Products(product_name,stock,price,category,expiry_date)
    VALUES(?,?,?,?,?)
    """,(product_name,stock,price,category,expiry_date)
    )

    conn.commit()
    conn.close()

    return {"message": "Product created successfully"}
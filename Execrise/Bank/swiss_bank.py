import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from mysql.connector import Error

# ==============================================
# Connection Part to MySQL WorkBench 8.0 CE
# ==============================================

try:
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="ca32icp"
    )

    if mydb.is_connected():
        print("Successfully Connected")

except Error as err:
    print(f"Try Again {err}")

finally:
    if "mydb" in locals() and mydb.is_connected():
        mydb.close()
        print("MySQL connection closed.")
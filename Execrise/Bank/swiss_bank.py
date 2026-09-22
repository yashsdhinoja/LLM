import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from mysql.connector import Error

# ==============================================
# Connection Part to MySQL WorkBench 8.0 CE
# ==============================================

# try:
#     mydb = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="ca32icp"
#     )

#     if mydb.is_connected():
#         print("Successfully Connected")

# except Error as err:
#     print(f"Try Again {err}")

# finally:
#     if "mydb" in locals() and mydb.is_connected():
#         mydb.close()
#         print("MySQL connection closed.")

# ==============================================
# OOPS Bank Account
# ==============================================

class BankAccount:
    def __init__(self, account_no, pin, intiler_balance, name):
        self.name = name
        self.account_no = account_no
        self.__pin = pin
        self.__balance = intiler_balance

    @property
    def balance(self):
        return self.__balance

    @staticmethod
    def validate_pin(pin_input):
        return pin_input.isdigit() and len(pin_input) == 4

    def verify_pin(self, entry_pin):
        return self.__pin == entry_pin

# ==============================================
# OOPS Tkinter Container 
# ==============================================

class SwissBankApp(tk.Tk):
    """The main window controller that manages screen switching."""

    def __init__(self):
        super().__init__()

        self.title("Swiss Bank Corporation")
        self.geometry("1400x1500")
        self.configure(bg="#ffffff")

        # Create a container frame that fills the entire window
        # All individual screens will be placed inside this container
        container = tk.Frame(self, bg="#ffffff")
        container.pack(side="top", fill="both", expand=True)

        # Configure rows/columns so screens fill the space properly
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Dictionary to store references to our screen frames
        self.frames = {}

        # List all the screen classes you want to initialize
        for ScreenClass in (LoginScreen):
            page_name = ScreenClass.__name__
            
            # Instantiate each screen inside the master container
            frame = ScreenClass(parent=container, controller=self)
            self.frames[page_name] = frame

            # Stack them in the exact same grid position (row 0, column 0)
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the initial screen on startup
        self.show_frame("LoginScreen")

    def show_frame(self, page_name):
        """Brings the requested screen frame to the front."""
        frame = self.frames[page_name]
        frame.tkraise()  # Pulls the frame to the top of the stack

class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ffffff")
        self.controller = controller

        # Title
        label = tk.Label(self, text="Secure Login", font=("Arial", 24, "bold"), bg="#ffffff", fg="#333333")
        label.pack(pady=40)

        # Username Field Example
        user_lbl = tk.Label(self, text="Username", font=("Arial", 12), bg="#ffffff")
        user_lbl.pack(anchor="w", padx=50)
        user_entry = tk.Entry(self, font=("Arial", 14), bd=1, relief="solid")
        user_entry.pack(fill="x", padx=50, pady=(0, 20))

        # Button to switch to Dashboard
        login_btn = tk.Button(
            self, 
            text="Login", 
            font=("Arial", 12, "bold"), 
            bg="#d9251c", # Swiss red
            fg="white", 
            relief="flat",
            command=lambda: controller.show_frame("MainDashboard")
        )
        login_btn.pack(fill="x", padx=50, pady=20)


# class MainDashboard(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, bg="#f8f9fa")
#         self.controller = controller

#         # Header
#         label = tk.Label(self, text="Yash Dhinoja", font=("Arial", 20, "bold"), bg="#f8f9fa", fg="#1a1a1a")
#         label.pack(pady=(30, 10))

#         balance_lbl = tk.Label(self, text="CHF 1,245,600.00", font=("Arial", 26, "italic"), bg="#f8f9fa", fg="#2e7d32")
#         balance_lbl.pack(pady=10)

#         # Navigation Buttons
#         transfer_btn = tk.Button(
#             self, text="Transfer Funds", font=("Arial", 12),
#             command=lambda: controller.show_frame("TransferScreen")
#         )
#         transfer_btn.pack(fill="x", padx=50, pady=10)

#         logout_btn = tk.Button(
#             self, text="Secure Logout", font=("Arial", 12), fg="red",
#             command=lambda: controller.show_frame("LoginScreen")
#         )
#         logout_btn.pack(fill="x", padx=50, pady=10)


# class TransferScreen(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, bg="#ffffff")
#         self.controller = controller

#         label = tk.Label(self, text="Make a Transfer", font=("Arial", 20, "bold"), bg="#ffffff")
#         label.pack(pady=30)

#         # Button to go back
#         back_btn = tk.Button(
#             self, text="← Back to Dashboard", font=("Arial", 12),
#             command=lambda: controller.show_frame("MainDashboard")
#         )
#         back_btn.pack(pady=20)


if __name__ == "__main__":
    app = SwissBankApp()
    app.mainloop()

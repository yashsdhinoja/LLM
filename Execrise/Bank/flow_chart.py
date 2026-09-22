# +-----------------------------------+
#                          |       Tkinter GUI Application     |
#                          |  (Login / Register / Dashboard)   |
#                          +-----------------+-----------------+
#                                            |
#                                            v
#                        +---------------------------------------+
#                        |   OOP Logic Layer (Bank & Customer)   |
#                        |  - Private Attributes (__balance, __pin)|
#                        |  - Methods (deposit, withdraw, etc.)  |
#                        |  - Static Methods (validation rules)  |
#                        +-------------------+-------------------+
#                                            |
#                                            v
#                         +-------------------------------------+
#                         |     Database Handler (MySQL 8.0)    |
#                         |   - Execute Queries (CRUD)          |
#                         |   - Manage Database Connection      |
#                         +------------------+------------------+
#                                            |
#                                            v
#                          +-----------------------------------+
#                          |       MySQL Workbench Database    |
#                          |   Tables: customers, transactions |
#                          +-----------------------------------+

# ===========================================================================================================================================

# Program Logic Flowchart
#                  +-----------------------------------+
#                  |            Start App              |
#                  +-----------------+-----------------+
#                                    |
#                                    v
#                          +-------------------+
#                          |  Main Tkinter Menu|
#                          +---------+---------+
#                                    |
#         +--------------------------+--------------------------+
#         |                          |                          |
#         v                          v                          v
# +---------------+          +---------------+          +---------------+
# | 1. Open A/C   |          |  2. Account   |          | 3. Exit App   |
# |   (Register)  |          |     Login     |          |               |
# +-------+-------+          +-------+-------+          +-------+-------+
#         |                          |                          |
#         v                          v                          v
#  [Enter Details]            [Enter A/C & PIN]               [End]
#         |                          |
#         v                          v
#  [Validate Input]           [Verify in MySQL]
#         |                          |
#         v                  +-------+-------+
#   [Save to MySQL           | Matches?      |
#    `customers`]            +---+-------+---+
#         |                      |       |
#         v                     Yes      No ---> [Display Error]
#  [Show A/C Number]             |
#         |                      v
#         +-------------> +---------------------------------------+
#                         |         Customer Dashboard            |
#                         +-------------------+-------------------+
#                                             |
#         +-------------------+---------------+-------------------+-------------------+
#         |                   |                                   |                   |
#         v                   v                                   v                   v
# +---------------+   +---------------+                   +---------------+   +---------------+
# | Check Balance |   | Transactions  |                   | Deposit /     |   | Close Account |
# |               |   |  (Passbook)   |                   | Withdraw      |   |               |
# +-------+-------+   +-------+-------+                   +-------+-------+   +-------+-------+
#         |                   |                                   |                   |
#         v                   v                                   v                   v
#  [Query Balance     [Fetch `transactions`               [Update `__balance` [Confirm Delete/
#   via Getter]        for Account]                        & Insert Log]       Deactivate]
#         |                   |                                   |                   |
#         v                   v                                   v                   v
#  [Display in GUI]   [Display Table/List]                [Commit MySQL Query] [Set Status='Closed'
#         |                   |                                   |             in MySQL]
#         +-------------------+---------------+-------------------+                   |
#                                             |                                       v
#                                             +--------------------------------> [Return to Main]


# 1. OOPs Architecture & Class Blueprint

# To organize your code cleanly, separate your business logic from your Tkinter UI. Build a core class (e.g., BankAccount) that uses encapsulation to manage customer state and private data.
# Private Attributes (__): Store __balance and __pin as private attributes so they cannot be modified directly from outside the class.
# Getters & Setters (@property): Use @property for balance so Tkinter can easily display the current balance, while keeping the setter restricted so negative or invalid changes are blocked.
# Static Methods (@staticmethod): Use static methods for standalone utility checks that do not depend on object instance state (e.g., verifying if an entered PIN is a 4-digit integer or if a newly opened account number is valid).


#  2. Transaction & Passbook Logic Flow
# Your passbook feature relies on logging every monetary event to MySQL immediately when it happens.
# Deposit / Withdrawal Logic:
# When a user inputs an amount in Tkinter, call a method on your BankAccount object (e.g., account.withdraw(amount)).
# Verify inside the method that amount > 0 and amount <= self.__balance.
# Update the internal private __balance.
# Execute an INSERT query into your MySQL transactions log table containing (account_no, transaction_type, amount, updated_balance, timestamp).
# Execute an UPDATE query on your customer data table to persist the new balance in MySQL.
# Passbook Rendering (Tkinter ttk.Treeview):
# Add a get_passbook() method to your OOP class that queries your MySQL transaction history table for rows matching self.account_no.
#  In your Tkinter GUI, fetch this list of tuple records from the method and loop through them to populate a ttk.Treeview widget (which acts as an interactive tabular passbook).



# 3. Account Opening & Closing Lifecycle Logic
# Opening an Account:
# Collect customer details via a Tkinter registration form.
# Use a @staticmethod to auto-generate or format a unique account number.
# Run an INSERT statement into MySQL to create the new account entry.
# Instantiate a new BankAccount object and navigate the user directly to the dashboard screen.
# Closing an Account:
# Require the customer to enter their PIN inside a confirmation pop-up window (messagebox or custom Tkinter modal).
# Perform a check using your internal PIN verification logic.
# Instead of permanently deleting the record from MySQL (which destroys historical audit data), update an account_status column in MySQL from 'ACTIVE' to 'CLOSED'.
# Destroy the current user session object in Tkinter and redirect the user back to the main login view.




# 4. Tkinter GUI Session Management
# Screen Navigation Logic: Use a single parent tk.Tk() window and swap tk.Frame containers for different views (e.g., LoginFrame, DashboardFrame, PassbookFrame).
# Active User State: When a user logs in successfully, query their details from MySQL Workbench, instantiate a global/session BankAccount instance, and pass that single object to all sub-frames in Tkinter.
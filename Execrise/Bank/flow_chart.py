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

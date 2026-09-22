
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

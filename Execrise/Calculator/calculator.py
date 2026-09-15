from tkinter import *
tk = Tk()
tk.title("Calculator")
tk.geometry("400x550")  # A more standard calculator size
tk.config(background="#e2e9f1")

# Main container frame
frame = Frame(tk, bg="#e2e9f1")
frame.pack(pady=15)  # Adds some space at the top

# 1. Create and Grid the Entry Box
# justify="right" makes the numbers appear on the right side like a real calculator
entry = Entry(frame, font=("Arial", 28), fg="#000000", bg="white", justify="right")

# columnspan=4 makes the text box stretch across all 4 columns of buttons
entry.grid(row=0, column=0, columnspan=4, ipady=15, pady=18, sticky="ew")

# 2. A map of our calculator buttons (Text, Row, Column)
button_layout = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# 3. Loop through the map and draw the buttons
for (btn_text, row, col) in button_layout:
    btn = Button(frame, text=btn_text, font=("Consolas", 17), width=5, height=2)
    
    # Put each button in its specific row and column
    btn.grid(row=row, column=col, padx=15, pady=15)

tk.mainloop()
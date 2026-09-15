import math
import tkinter as tk

# --- 1. GLOBAL STATE VARIABLES ---
# These variables act as the "memory" of our calculator
first_number = 0
math_operator = ""

# --- 2. FUNCTIONS ---

def button_click(number):
    # This just types numbers onto the screen
    entry.insert(tk.END, str(number))

def clear():
    entry.delete(0, tk.END)

def button_operator(operator):
    # Tell Python we want to modify our global memory variables
    global first_number
    global math_operator
    
    if entry.get() != "":
        first_number = float(entry.get())
        math_operator = operator
        entry.delete(0, tk.END)

def calculator():
    # 1. Get the second number that the user just typed
    if entry.get() != "" and math_operator != "":
        second_number = float(entry.get())
        entry.delete(0, tk.END)
        
    # 3. Check our memory to see which math operation to perform
    if math_operator == '+':
        entry.insert(0, first_number + second_number)
        
    elif math_operator == '-':
        entry.insert(0, first_number - second_number)
        
    elif math_operator == 'x':
        entry.insert(0, first_number * second_number)
        
    elif math_operator == '/':
        if second_number == 0:
            entry.insert(0, "Error")
        else:
            entry.insert(0, first_number / second_number)

def button_sin():
    if entry.get() != "":
        current_number = float(entry.get())
        radians = math.radians(current_number)
        ans = math.sin(radians)
        entry.delete(0, tk.END)
        entry.insert(0, str(ans))

def button_cos():
     if entry.get() != "":
        current_number = float(entry.get())
        result = math.cos(math.radians(current_number))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))  

def button_tan():
    if entry.get() != "":
        current_number = float(entry.get())
        result = math.tan(math.radians(current_number))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))

def button_rad():
    if entry.get() != "":
        current_number = float(entry.get())
        result = math.radians(current_number)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))

root = tk.Tk()
root.title("Number Pad")
    
# 2. Create the Entry widget
entry = tk.Entry(root, font=("Arial", 28), fg="#000000", bg="white", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipady=15, pady=18, sticky="ew")


# 1. Create a "Map" of all your buttons (Text, Row, Column)
button_layout = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
    ('3', 3, 0), ('2', 3, 1), ('1', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('00', 4, 1), ('AC', 4, 2), ('+', 4, 3),
    ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('rad', 5, 3),
    ('.', 6, 0),
    ('=', 7, 0), 
]

# 2. Run the For Loop
for (text, row, col) in button_layout:
    
    # Check if the button is special ("C" or "=") so it gets the right function
    if text == 'AC':
        action = clear

    elif text == '=':
        # Assuming you will make a calculate() function next!
        action = calculator

    elif text == 'sin':
            action = button_sin

    elif text == 'cos':
            action = button_cos

    elif text == 'tan':
            action = button_tan

    elif text == 'rad':
            action = button_rad

    elif text in ['/', 'x', '-', '+']:
        action = lambda t=text: button_operator(t)

    else:
        # The MAGIC fix for the loop bug: t=text
        action = lambda t=text: button_click(t)
    
    # 3. Create and place the button dynamically
    if text == "=":
        btn = tk.Button(root, text=text, padx=40, pady=20, command=action)
        btn.grid(row=row, column=col, columnspan=4, sticky="ew")

    else:
        btn = tk.Button(root, text=text, padx=40, pady=20, command=action)
        btn.grid(row=row, column=col)

root.mainloop()
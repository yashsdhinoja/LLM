import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Traffic Light")
root.geometry("200x450")
root.configure(bg="#2c3e50")

# Create a canvas to draw the traffic light body and lamps
canvas = tk.Canvas(root, width=160, height=400, bg="#34495e", highlightthickness=0)
canvas.pack(pady=25)

# Draw the background frame of the traffic light
canvas.create_rectangle(10, 10, 150, 390, fill="#1a252f", outline="#11181f", width=4)

# Draw the three light circles (initially off/dark)
red_light = canvas.create_oval(30, 20, 130, 120, fill="#4a0000", outline="#11181f", width=2)
yellow_light = canvas.create_oval(30, 140, 130, 240, fill="#4a4a00", outline="#11181f", width=2)
green_light = canvas.create_oval(30, 260, 130, 360, fill="#004a00", outline="#11181f", width=2)

# Track the current state of the traffic light
# 0 = Red, 1 = Green, 2 = Yellow
current_state = 0

def update_traffic_light():
    global current_state
    
    # Reset all lights to their dark/off colors
    canvas.itemconfig(red_light, fill="#4a0000")
    canvas.itemconfig(yellow_light, fill="#4a4a00")
    canvas.itemconfig(green_light, fill="#004a00")
    
    # Turn on the active light and set the delay for the next change
    if current_state == 0:
        canvas.itemconfig(red_light, fill="#ff0000")  # Bright Red
        current_state = 1
        delay = 4000  # Red stays on for 4 seconds
    elif current_state == 1:
        canvas.itemconfig(green_light, fill="#00ff00") # Bright Green
        current_state = 2
        delay = 3000  # Green stays on for 3 seconds
    else:
        canvas.itemconfig(yellow_light, fill="#ffff00") # Bright Yellow
        current_state = 0
        delay = 1500  # Yellow stays on for 1.5 seconds
        
    # Schedule the next state transition
    root.after(delay, update_traffic_light)

# Start the traffic light cycle
update_traffic_light()

# Run the Tkinter event loop
root.mainloop()
import tkinter as tk
root = tk.Tk()
root.title("Traffic_Signal")
root.geometry("600x600") # Resized for better visibility
root.configure(bg="#ffffff")

# 1. Create the Canvases
traffic_signal_top = tk.Canvas(root, width=80, height=150, bg="#000000", highlightthickness=0)
traffic_signal_top.pack(side="top", pady=10)

traffic_signal_left = tk.Canvas(root, width=80, height=150, bg="#000000", highlightthickness=0)
traffic_signal_left.pack(side="left", padx=20)

traffic_signal_right = tk.Canvas(root, width=80, height=150, bg="#000000", highlightthickness=0)
traffic_signal_right.pack(side="right", padx=20)

traffic_signal_bottom = tk.Canvas(root, width=80, height=150, bg="#000000", highlightthickness=0)
traffic_signal_bottom.pack(side="bottom", pady=10)

all_canvas = [
        {"name": "top", "canvas": traffic_signal_top},
        {"name": "right", "canvas": traffic_signal_right},
        {"name": "bottom", "canvas": traffic_signal_bottom},
        {"name": "left", "canvas": traffic_signal_left}]

signals_list = []

for item in all_canvas:
    canvas = item["canvas"]
    canvas.create_rectangle(0, 0, 80, 150, fill="#CED7DF", outline="#11181f", width="4")
    r_id = canvas.create_oval(10, 10, 70, 50, fill="#4a0000", outline="#11181f", width="2")
    y_id = canvas.create_oval(10, 55, 70, 95, fill="#4a4a00", outline="#11181f", width="2")
    g_id = canvas.create_oval(10, 100, 70, 140, fill="#004a00", outline="#11181f", width="2")

    signals_list.append({
        "name": item["name"],
        "canvas":canvas,
        "red":r_id,
        "yellow":y_id,
        "green":g_id
    })

def set_all_to_red():
    for signal in signals_list:
        canvas = signal["canvas"]
        canvas.itemconfig(signal["red"], fill="#ff0000")
        canvas.itemconfig(signal["yellow"], fill="#4a4a00")
        canvas.itemconfig(signal["green"], fill="#004a00")

def traffic_cycle(active_index=0, stage="green"):
    # First set every single signal to bright red safety state
    set_all_to_red()
    
    # Target the single active signal
    active_signal = signals_list[active_index]
    canvas = active_signal["canvas"]

    if stage == "green":
        # Turn off Red, turn on Green for this signal only
        canvas.itemconfig(active_signal["red"], fill="#4a0000")
        canvas.itemconfig(active_signal["green"], fill="#00ff00")
        
        # Keep it green for 4 seconds, then switch to yellow
        root.after(4000, lambda: traffic_cycle(active_index, "yellow"))

    elif stage == "yellow":
        # Turn off Green, turn on Yellow for this signal only
        canvas.itemconfig(active_signal["red"], fill="#4a0000")
        canvas.itemconfig(active_signal["yellow"], fill="#ffff00")
        
        # Keep it yellow for 1.5 seconds, then move to the NEXT signal's green stage
        next_index = (active_index + 1) % len(signals_list) # Loops back to 0 after index 3
        root.after(1500, lambda: traffic_cycle(next_index, "green"))

# Start the cycle with the first signal (Top) going Green
traffic_cycle(0, "green")
root.mainloop()
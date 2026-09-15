# 3. Loop through the map and draw the buttons
for (btn_text, row, col) in button_layout:
    btn = Button(frame, text=btn_text, font=("Consolas", 15), width=5, height=2)

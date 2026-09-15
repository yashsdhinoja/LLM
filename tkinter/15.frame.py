from tkinter import *

window = Tk()

frame = Frame(window, bg="black", bd=1, relief=SUNKEN)
frame.place(x=100, y=100)

Button(frame, text="W", font=("Consolas", 25), width=3).pack()

window.mainloop()
from tkinter import *

count = 0

def click():
    global count
    count += 1
    print("You Click Button !!!")
    print(count)

tk = Tk()

image = PhotoImage(file="Screenshot 2026-07-23 134240.png")

button = Button(tk,
                command=click,
                font=("Roboto"),
                fg="#00FF00",
                bg="yellow",
                activeforeground="#00FF00",
                activebackground="#11FF11",
                state=ACTIVE,
                image=image,
                compound="top" )
button.pack()

tk.mainloop()
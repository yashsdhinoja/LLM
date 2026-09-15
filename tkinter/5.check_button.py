from tkinter import *

def display():
    if(a.get()==1):
        print("Fire !!!")
    else:
        print("Try Again")
tk = Tk()

a = IntVar()
Check_button = Checkbutton(tk, 
                           text="I Agree to Something",
                           variable=a,
                           onvalue=1,
                           offvalue=0,
                           command=display
                           )

Check_button.pack()
tk.mainloop()
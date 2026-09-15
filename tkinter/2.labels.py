from tkinter import *

# label = An Area Widget that holds text and/or an image within a window

tk = Tk()
photo = PhotoImage(file='Screenshot 2026-07-03 175449.png')
tk.geometry("420x420")

# label = Label(tk, text="Hello")
# label.pack()

label = Label(tk, 
              text="Yash Dhinoja", 
              font=('Arial',40,'italic','underline'),  # font name, size, line
              fg='yellow', #text color
              bg='orange', # text bg color
              relief=RAISED, # border option RAISED, SUNKEN 
              bd=4, # border width size
              padx=1, # padding in x-axis
              pady=1,  # padding in y-axis
              image=photo, # image is decalred 
              compound='top'
            )

label.place(x=45,y=30)

tk.mainloop()
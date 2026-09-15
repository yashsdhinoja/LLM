from tkinter import *
# entry widget = textbox that accepts a single line of user input

def submit():
    username = entry.get()
    print("Hello" +  username)
    entry.config(state=DISABLED)  


def delete():
    entry.delete(0,END) # all texts in delete at once's click


def backspace():
    entry.delete(len(entry.get())-1, END) # one by one is delete the texts


window = Tk()
window.geometry("620x620")


entry = Entry(window,   
              font=("Arial",18), 
              fg="#11FF00", 
              bg="green",
              show="*")
entry.pack(side=LEFT)


submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)


delete_button = Button(window,text="delete",command=delete)
delete_button.pack(side=RIGHT)


backspace_button = Button(window,text="backspace",command=backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()
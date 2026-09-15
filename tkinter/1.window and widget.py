from tkinter import * 

# widget = GUI elements: Buttons, Textboxes, labels, images
# windows = server as a container to hold or contain these widgets

# instantiate an instance of a window, should not display the window
window = Tk() 

# width and height of window
window.geometry("420x420") 

# Name Title of window
window.title("Yash") 

# replace the icon with photo name 
icon = PhotoImage(file='Screenshot 2026-07-03 175449.png')
window.iconphoto(True,icon)

# change background color of window, currently show the white
window.config(background="#96e0d4")

# place window on computer screen. listen for events
window.mainloop() 
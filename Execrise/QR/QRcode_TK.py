import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def click():
    link = entry.get()

    if link == "":
        messagebox.showwarning("Error", "Please entry the link")
    else:
        qr_img = qrcode.make(link)
        qr_img = qr_img.resize((200, 200))
        tk_img = ImageTk.PhotoImage(qr_img) 
        qr_label.config(image=tk_img)
        qr_label.image = tk_img

root = tk.Tk()
root.title("QR Scanner")
root.geometry("500x500")

instruction = tk.Label(root, text="Enter the Link : ", font=("Arial", 14))
instruction.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 24))
entry.pack(pady=10)

button = tk.Button(command=click,text="Submit", font=("Roboto"), fg="#000000", bg="yellow", activeforeground="#EAF3EA", activebackground="#FFFFFF")
button.pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
import tkinter as tk
from tkinter import *
from tkinter import ttk

def button_clicked():
    num = int(integer_field.get())
    print(f"The value entered is {num}")

root = tk.Tk()
root.geometry("300x150")

integer_field = tk.Entry(root)
integer_field.pack(pady=10)

button = tk.Button(root, text="Click me", command=button_clicked)
button.pack(pady=20)

lb = Listbox(root)
lb.pack("pipi", "popo", "papa", "pupu")


root.mainloop()

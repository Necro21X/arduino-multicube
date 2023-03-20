import tkinter as tk

def button_clicked():
    num = int(integer_field.get())
    print(f"The value entered is {num}")

root = tk.Tk()
root.geometry("300x150")

integer_field = tk.Entry(root)
integer_field.pack(pady=10)

button = tk.Button(root, text="Click me", command=button_clicked)
button.pack(pady=20)

root.mainloop()

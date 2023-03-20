import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.title("LED Cube Writer")

def fileCreate():
    name = name_field.get()
    open(name+'.ino', "x")
    with open('4.ino', 'r') as source, open(name +'.ino', 'w') as destination:
        lines = source.readlines()
        for line in lines[0:26]:
            destination.write(line)

    source.close()
    destination.close()
    
def lightsOn():
    x = xcoord.get()
    y = ycoord.get()
    print(x)
    print(y)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

message_filename = tk.Label(mainframe, text="Filename:")
message_filename.grid(column=1, row=1, sticky=W)

name_field = tk.Entry(mainframe)
name_field.grid(column=2, row=1, sticky=(W, E))

button_create = ttk.Button(mainframe, text="Create Cofing File", command=fileCreate)
button_create.grid(column=3, row=1, sticky=E)

message_coord = tk.Label(mainframe, text="X/Y Coordinate")
message_coord.grid(column=1, row=2, sticky=W)

xcoord = IntVar()
num_xcoord = tk.Entry(mainframe, textvariable=xcoord)
num_xcoord.grid(column=2, row=2, sticky=W)

ttk.Label(mainframe, text="/").grid(column=3, row=2, sticky=W)

ycoord = IntVar()
num_ycoord = tk.Entry(mainframe, textvariable=ycoord)
num_ycoord.grid(column=4, row=2, sticky= W)

button_coord = ttk.Button(mainframe, text="Lights on!", command=lightsOn)
button_coord.grid(column=5, row=2, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()

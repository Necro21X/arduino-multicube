import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.title("LED Cube Writer")
list = []
listVar = StringVar(value=list)
linecounter = 0

def fileCreate():
    name = name_field.get()
    fileNum = fileNum_field.get()
    open(name+'.ino', "x")
    with open(fileNum+'.ino', 'r') as source, open(name +'.ino', 'w') as destination:
        lines = source.readlines()
        for line in lines[0:26]:
            destination.write(line)

    source.close()
    destination.close()

def lightsOn():
    global linecounter
    x = xcoord.get()   
    y = ycoord.get()
    name = name_field.get()
    with open(name+ '.ino', 'a') as destination:
      destination.write('setCoord('+str(x)+', '+str(y)+');\n')
    linecounter = linecounter + 1
    destination.close()
    lbox.insert(END, 'Tower: '+str(x)+'/'+str(y))
    
def planeOn():
    global linecounter
    z = zcoord.get() 
    name = name_field.get()
    with open(name+'.ino', 'a') as destination:
        destination.write('setPlane('+str(z)+');\n')
    linecounter = linecounter + 1
    destination.close()
    lbox.insert(END, 'Plane: '+str(z))

def addDelay():
    global linecounter; d = delay.get()
    name = name_field.get()
    with open(name+ '.ino', 'a') as destination:
        destination.write('shiftRegisters(); delay('+str(d)+'); stopRegisters();\n')
    linecounter = linecounter + 1
    destination.close
    lbox.insert(END, 'Delay: '+str(d))

def finishCode():
    name = name_field.get()
    fileNum = fileNum_field.get()
    with open(fileNum+'.ino', 'r') as source, open(name+'.ino', 'a') as destination:
        lines = source.readlines()
        for line in lines[26:64]:
            destination.write(line)
    source.close()
    destination.close()
    
def deleteLine():
    global linecounter
    selectedLines = lbox.curselection()
    deleteLine = selectedLines
    name = name_field.get()
    for deleteLine in selectedLines:
        lbox.delete(deleteLine)
        with open(name + '.ino', 'r') as destination:
            inputText = destination.readlines()
            del inputText[deleteLine+26]
        destination.close()
        with open(name + '.ino', 'w') as destination:
            lindex = 1
            for textline in inputText:
                destination.write(textline)
        destination.close()
    print("Successfully deleted!")
           
    linecounter = linecounter - 1
    
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

tk.Label(mainframe, text="Filename:").grid(column=1, row=1, sticky=W)

name = StringVar()
name_field = ttk.Entry(mainframe, textvariable=name)
name_field.grid(column=2, row=1, sticky=(W, E))

tk.Label(mainframe, text="Cube Size:").grid(column=3, row=1, sticky=W)

fileNum = StringVar()
fileNum_field = ttk.Entry(mainframe, textvariable=fileNum)
fileNum_field.grid(column=4, row=1, sticky=W)

button_create = ttk.Button(mainframe, text="Create Cofing File", command=fileCreate)
button_create.grid(column=5, row=1, sticky=E)

message_coord = tk.Label(mainframe, text="X/Y Coordinates:")
message_coord.grid(column=1, row=2, sticky=W)

xcoord = IntVar()
num_xcoord = ttk.Entry(mainframe, textvariable=xcoord)
num_xcoord.grid(column=2, row=2, sticky=W)

ttk.Label(mainframe, text="/").grid(column=3, row=2, sticky=W)

ycoord = IntVar()
num_ycoord = ttk.Entry(mainframe, textvariable=ycoord)
num_ycoord.grid(column=4, row=2, sticky= W)

button_coord = ttk.Button(mainframe, text="Light LED", command=lightsOn)
button_coord.grid(column=5, row=2, sticky=E)

ttk.Label(mainframe, text="Plane:").grid(column=1, row=3, sticky=W)

zcoord = IntVar()
num_plane = ttk.Entry(mainframe, textvariable=zcoord)
num_plane.grid(column=2, row=3, sticky=W)

button_plane = ttk.Button(mainframe, text="Light Plane", command=planeOn)
button_plane.grid(column=3, row=3, sticky=E)

lbox = Listbox(mainframe, listvariable=list, height=8)
lbox.grid(column=4, row=3, columnspan=2, rowspan=2)

button_delete = ttk.Button(mainframe, text="Delete Selected", command=deleteLine)
button_delete.grid(column=6, row=3, sticky=(N, E))

button_finish = ttk.Button(mainframe, text="Finish Code", command=finishCode)
button_finish.grid(column=6, row=4, sticky=(N, E))

ttk.Label(mainframe, text="Delay:").grid(column=1, row=4, sticky=W)

delay = IntVar()
num_delay = ttk.Entry(mainframe, textvariable=delay)
num_delay.grid(column=2, row=4, sticky=W)

button_delay = ttk.Button(mainframe, text="Add Delay", command=addDelay)
button_delay.grid(column=3, row=4, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()

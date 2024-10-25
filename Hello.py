# Importer Tkinter-modulet
from tkinter import *

# Initialiser hovedvinduet
root = Tk()

# Opret Label-widgets med tekst
myLabel1 = Label(root, text="Hello World")             # Første label med tekst
myLabel2 = Label(root, text="My Name is John Elder")    # Anden label med tekst
myLabel3 = Label(root, text="              ")           # Tredje label med tom plads for justering

# Placer labels på skærmen ved hjælp af grid layout manager
myLabel1.grid(row=0, column=0)           # Placerer myLabel1 i første række, første kolonne
myLabel2.grid(row=1, column=5)           # Placerer myLabel2 i anden række, femte kolonne (til højre)
myLabel3.grid(row=1, column=1)           # Placerer myLabel3 i anden række, første kolonne (til mellemrum)

# Start hovedloopet for at vise GUI
root.mainloop()

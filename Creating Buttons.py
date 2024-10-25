# Importer nødvendige biblioteker
from tkinter import *  # Importer alle klasser og funktioner fra tkinter

# Opret hovedvinduet
root = Tk()  # Initialiser hovedvinduet

# Definer en funktion, der skal kaldes, når knappen klikkes
def myClick():
    # Opret en Label, der viser en besked
    myLabel1 = Label(root, text="Look! I clicked a Button!!")  # Opret en Label med tekst
    myLabel1.pack()  # Placer Label i hovedvinduet

# Opret en knap, der kalder myClick-funktionen, når den klikkes
myButton = Button(root, text="Click Me!", command=myClick)  # Opret en knap med tekst og tilknyttede funktion
myButton.pack()  # Placer knappen i hovedvinduet

# Start hovedløkken for GUI
root.mainloop()  # Kør GUI-programmet, indtil det lukkes
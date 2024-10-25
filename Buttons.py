# Importer nødvendige biblioteker
from tkinter import *  # Importer alle klasser og funktioner fra tkinter

# Opret hovedvinduet
root = Tk()  # Initialiser hovedvinduet

# Opret en Entry widget til at indtaste navn
e = Entry(root, width=50, bg="blue", fg="white", borderwidth=5)  # Opret en Entry med specifik bredde, baggrundsfarve og tekstfarve
e.pack()  # Placer Entry i hovedvinduet
e.insert(0, "Enter Your Name: ")  # Indsæt en standardtekst i Entry

# Definer en funktion, der kaldes, når knappen klikkes
def myClick():
    hello = "Hello " + e.get()  # Hent teksten fra Entry og tilføj "Hello "
    myLabel1 = Label(root, text=hello)  # Opret en Label med den hilsende tekst
    myLabel1.pack()  # Placer Label i hovedvinduet

# Opret en knap, der kalder myClick-funktionen, når den klikkes
myButton = Button(root, text="Enter Your Name", command=myClick, fg="blue", bg="#ffffff")  # Opret en knap med tekst og tilknyttede funktion
myButton.pack()  # Placer knappen i hovedvinduet

# Start hovedløkken for GUI
root.mainloop()  # Kør GUI-programmet, indtil det lukkes
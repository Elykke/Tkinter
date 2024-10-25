# Importer nødvendige moduler
from tkinter import *                 # Tkinter bruges til at oprette GUI
from PIL import ImageTk, Image         # Pillow bruges til at håndtere billeder i tkinter

# Initialiser hovedvinduet
root = Tk()
root.title('Learn To Code at Codemy.com')   # Sætter vinduets titel
root.iconbitmap('')                         # Tilføj en sti til et ikon her, hvis nødvendigt

# Definer en liste over valg (til pizza toppings) og standardvalget for radioknapperne
MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()           # Variabel til at holde værdien af den valgte radioknap
pizza.set("Pepperoni")        # Standardværdi for radioknapperne

# Opret radioknapper for hver topping i MODES-listen
for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

# Definer en funktion, der viser den valgte topping, når knappen "Click Me!" trykkes
def clicked(value):
    myLabel = Label(root, text=value)     # Label viser den valgte værdi
    myLabel.pack()

# Opret en knap, der viser det aktuelle valg, når der klikkes på den
myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

# Start hovedloopet, der viser vinduet og holder det åbent
root.mainloop()

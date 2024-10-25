from tkinter import *  # Importer alle klasser og funktioner fra tkinter
from PIL import ImageTk, Image  # Importer ImageTk og Image fra PIL (Python Imaging Library)

# Opret hovedvinduet
root = Tk()  
root.title("Lorem ipsum")  # Sæt titlen på vinduet
root.iconbitmap('c:/gui/codemy.ico')  # Sæt ikonet for vinduet (fuld sti til ikonet)


# Indlæs et billede og opret et PhotoImage objekt
my_img = ImageTk.PhotoImage(Image.open("aspen.png"))  # Åbn billedet "aspen.png" og konverter det til et PhotoImage objekt
my_label = Label(image=my_img)  # Opret en Label widget med billedet
my_label.pack()  # Placer Label widgeten i vinduet


# Opret en knap til at afslutte programmet
button_quit = Button(root, text="Exit Program", command=root.quit)  # Opret en knap med teksten "Exit Program", der afslutter programmet
button_quit.pack()  # Placer knappen i vinduet


# Start hovedløkken for tkinter, som venter på brugerinteraktion
root.mainloop()  
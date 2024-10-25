# Importer nødvendige biblioteker
from tkinter import *  # Importer alle klasser og funktioner fra tkinter
from PIL import ImageTk, Image  # Importer ImageTk og Image fra PIL (Python Imaging Library)

# Opret hovedvinduet
root = Tk()  # Initialiser hovedvinduet
root.title('Learn To Code at Codemy.com')  # Sæt titlen på vinduet
root.iconbitmap('')  # Sæt et ikon for vinduet (ingen fil angivet her)

# Opret en LabelFrame for at gruppere widgets
frame = LabelFrame(root, padx=50, pady=50)  # Opret en LabelFrame med padding
frame.pack(padx=10, pady=10)  # Placer LabelFrame i hovedvinduet med padding

# Opret knapper
b = Button(frame, text="Don't click here!")  # Opret en knap med tekst
b2 = Button(frame, text="... or here!")  # Opret en anden knap med tekst

# Placer knapperne i LabelFrame med grid layout
b.grid(row=0, column=0)  # Placer den første knap i række 0, kolonne 0
b2.grid(row=1, column=1)  # Placer den anden knap i række 1, kolonne 1

# Start hovedløkken for GUI
root.mainloop()  # Kør GUI-programmet, indtil det lukkes
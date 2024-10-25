from tkinter import *
from PIL import ImageTk, Image

# Opret hovedvinduet
root = Tk()
root.title("Lorem ipsum")  # Sæt titlen på vinduet
root.iconbitmap('c:/gui/codemy.ico')  # Sæt ikonet for vinduet

# Indlæs billeder
my_img1 = ImageTk.PhotoImage(Image.open("images/aspen.png"))  # Indlæs første billede
my_img2 = ImageTk.PhotoImage(Image.open("images/aspen2.png"))  # Indlæs andet billede
my_img3 = ImageTk.PhotoImage(Image.open("images/me1.png"))     # Indlæs tredje billede
my_img4 = ImageTk.PhotoImage(Image.open("images/me2.png"))     # Indlæs fjerde billede
my_img5 = ImageTk.PhotoImage(Image.open("images/me3.png"))     # Indlæs femte billede

# Opret en liste over billeder til navigation
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# Initialiser label til at vise det første billede
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)  # Placer label i gitteret

# Funktion til at gå til det næste billede
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    # Skjul det aktuelle billede
    my_label.grid_forget()
    # Opret en ny label til det næste billede
    my_label = Label(image=image_list[image_number - 1])
    # Opret knapper til navigation
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    # Deaktiver fremadknappen, hvis det er det sidste billede
    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    # Vis den nye label og knapper
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

# Funktion til at gå til det forrige billede
def back(image_number):
    global my_label
    global button_forward
    global button_back

    # Skjul det aktuelle billede
    my_label.grid_forget()
    # Opret en ny label til det forrige billede
    my_label = Label(image=image_list[image_number - 1])
    # Opret knapper til navigation
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    # Deaktiver tilbageknappen, hvis det er det første billede
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    # Vis den nye label og knapper
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

# Opret knapper til navigation og afslutning
button_back = Button(root, text="<<", command=back, state=DISABLED)  # Tilbageknappen starter deaktiveret
button_exit = Button(root, text="Exit Program", command=root.quit)   # Afslutningsknap
button_forward = Button(root, text=">>", command=lambda: forward(2))  # Fremadknap

# Placer knapperne i gitteret
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

# Start hovedsløjfen
root.mainloop()

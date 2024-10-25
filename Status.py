from tkinter import *
from PIL import ImageTk, Image  # Importering af nødvendige biblioteker

# Initialiser hovedvinduet
root = Tk()
root.title("Lorem ipsum")
root.iconbitmap('c:/gui/codemy.ico')  # Fuldt filsti til ikon

# Læs og opret billeder
my_img1 = ImageTk.PhotoImage(Image.open("images/aspen.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/aspen2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/me1.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/me2.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/me3.png"))

# Opret en liste til nem håndtering af billederne
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# Statuslinje, der viser hvilket billede der vises
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

# Opret en etiket til at vise det første billede
my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)

# Funktion til at opdatere statuslinje og knapper
def update_status(image_number):
    status.config(text="Image " + str(image_number) + " of " + str(len(image_list)))

# Funktion til at håndtere frem-knappen
def forward(image_number):
    global my_label, button_forward, button_back
    
    # Fjern det nuværende billede og vis det næste
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    
    # Opdater frem og tilbage knapper
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    # Deaktiver frem-knappen, hvis det sidste billede vises
    if image_number == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)
    
    # Vis det nye billede og knapper
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Opdater statuslinjen
    update_status(image_number)

# Funktion til at håndtere tilbage-knappen
def back(image_number):
    global my_label, button_forward, button_back

    # Fjern det nuværende billede og vis det forrige
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    
    # Opdater frem og tilbage knapper
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    # Deaktiver tilbage-knappen, hvis det første billede vises
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    # Vis det nye billede og knapper
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Opdater statuslinjen
    update_status(image_number)

# Initialiser knapperne og placér dem i layoutet
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

# Placér knapper og statuslinje
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

# Start hovedløkken
root.mainloop()

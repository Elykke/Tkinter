from tkinter import *

# Initialiser hovedvinduet
root = Tk()
root.title("Simple Calculator")  # Sætter titlen på vinduet

# Opretter en entry-widget til at vise input/output
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Variabler til at holde det første tal og typen af operation
f_num = None
math = ""

# Funktion til at håndtere tal-knapperne
def button_click(number):
    current = e.get()  # Hent det nuværende input fra entry
    e.delete(0, END)  # Ryd entry
    e.insert(0, str(current) + str(number))  # Indsæt det nye tal

# Funktion til at rydde entry
def button_clear():
    e.delete(0, END)  # Rydder hele indholdet af entry

# Funktion til at sætte operationen (addition, subtraktion, osv.)
def set_operation(op):
    global f_num, math
    f_num = float(e.get())  # Gemmer det første tal som float
    math = op  # Gemmer operationen
    e.delete(0, END)  # Rydder entry

# Funktion til at beregne resultatet
def button_equal():
    second_number = e.get()  # Henter det andet tal
    e.delete(0, END)  # Rydder entry

    try:
        # Udfører den valgte operation
        if math == "addition":
            e.insert(0, f_num + float(second_number))
        elif math == "subtraction":
            e.insert(0, f_num - float(second_number))
        elif math == "multiplication":
            e.insert(0, f_num * float(second_number))
        elif math == "division":
            if float(second_number) == 0:  # Tjek for division med nul
                e.insert(0, "Error")  # Vis fejl, hvis division med nul
            else:
                e.insert(0, f_num / float(second_number))
    except ValueError:  # Tjek for ugyldige input
        e.insert(0, "Error")  # Vis fejl for ugyldig input

# Definerer knapperne
buttons = [
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('0', 4, 0), ('+', 5, 0), ('=', 5, 1), ('Clear', 4, 1),
    ('-', 6, 0), ('*', 6, 1), ('/', 6, 2)
]

# Opretter og placerer knapperne
for (text, row, column) in buttons:
    if text == 'Clear':  # Hvis knappen er "Clear"
        button = Button(root, text=text, padx=79, pady=20, command=button_clear)
    elif text == '=':  # Hvis knappen er "="
        button = Button(root, text=text, padx=91, pady=20, command=button_equal)
    elif text in ('+', '-', '*', '/'):  # Hvis knappen er en operation
        button = Button(root, text=text, padx=39 if text == '+' else 40, pady=20, 
                        command=lambda op=text: set_operation(op))  # Sætter operationen
    else:  # For tal-knapperne
        button = Button(root, text=text, padx=40, pady=20, command=lambda num=text: button_click(num))
    button.grid(row=row, column=column)  # Placerer knappen i vinduet

# Starter GUI-løkken
root.mainloop()

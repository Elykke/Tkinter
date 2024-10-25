import turtle  # Importer turtle-modulet til grafisk tegning


# Initialiser turtle
t = turtle.Pen()  # Opret en ny pen (turtle)
t.speed(0)  # Sæt hastigheden til den hurtigste
t.turtlesize(2, 2, 2)  # Sæt størrelsen på turtle (pen)


# Funktion til at ændre farven
def change_color(color):
    t.color(color)  # Ændrer turtle's farve til den angivne farve


# Funktion til at ændre farven til rød
def color_red():
    change_color("red")  # Kalder change_color med "red"


# Funktion til at ændre farven til blå
def color_blue():
    change_color("blue")  # Kalder change_color med "blue"


# Funktion til at ændre farven til grøn
def color_green():
    change_color("green")  # Kalder change_color med "green"


# Funktion til at ændre farven til sort
def color_black():
    change_color("black")  # Kalder change_color med "black"


# Funktion til at ændre farven til hvid
def color_white():
    change_color("white")  # Kalder change_color med "white"


# Funktion til at bevæge sig fremad
def fremad():
    t.forward(50)  # Flytter turtle 50 enheder fremad


# Funktion til at dreje til venstre
def venstre():
    t.left(90)  # Drejer turtle 90 grader til venstre


# Funktion til at dreje til højre
def højre():
    t.right(90)  # Drejer turtle 90 grader til højre


# Funktion til at fortryde den seneste bevægelse eller drejning
def fortryd():
    t.undo()  # Fortryder den sidste handling


# Binding af funktioner til tastetryk
turtle.onkeypress(fremad, "Up")  # Binder fremad-funktionen til "Up" pilen
turtle.onkeypress(venstre, "Left")  # Binder venstre-funktionen til "Left" pilen
turtle.onkeypress(højre, "Right")  # Binder højre-funktionen til "Right" pilen
turtle.onkeypress(fortryd, "Down")  # Binder fortryd-funktionen til "Down" pilen
turtle.onkeypress(color_black, "1")  # Binder farveændring til sort til tast 1
turtle.onkeypress(color_red, "2")  # Binder farveændring til rød til tast 2
turtle.onkeypress(color_blue, "3")  # Binder farveændring til blå til tast 3
turtle.onkeypress(color_green, "4")  # Binder farveændring til grøn til tast 4
turtle.onkeypress(color_white, "5")  # Binder farveændring til hvid til tast 5

turtle.listen()  # Begynd at lytte efter tastetryk
turtle.done()  # Afslut turtle-grafikken

from turtle import *           #Bibliothek wird eingebunden

print("dadad")           #so macht man kommentare
print("Hello Word")

print()                  #leer
kleidung = "T-shirt"     #Variabeln deklarieren
print(kleidung)

print()

andrede = "Hey"         #String = Wörter
name = "Stella"

ganze_anrede = andrede + " " + name     #Strings aneinadner hängen
print(ganze_anrede)

print()

name = "Simon"
vier_mal_simon = 4 * name       #Strings können multipliziert werden
print(vier_mal_simon)

print()

name = 'Simon und Stella'       #es gehen auch einfache '
zeichen_anzahl = len(name)      #gibt die zahl an wielange die variable ist
print(zeichen_anzahl)

print()

person = "Stella"
satz = f"{person} singt gerne."     #lückenhalter/geht aber auch anders
satz = person + " singt gerne."
print(satz)

print()

person = "Simon"
speise = "Kuchen"
satz = f"{person} isst {speise}, weil er {speise} mag."     #geht auch mit mehreren Variabeln
print(f"{person} isst {speise}, weil er {speise} mag.")     #alles in print geht auch
#print(satz)
print()

zahl = 5                    #int, für einfache zahlen
print(zahl)

print()

gleitkommazahl = 2.5        #float für komma zahlen
print(gleitkommazahl)

print()

print(6 + 4)                #Rechenen, wenn du das nicht checkst bist du komisch
print(6 - 4) 
print(6 * 4) 
print(6 / 4) 
print(4 + (3 - 1) * 5)

print()

alter = 12
alter = alter + 1           #Varaibeln erhöhen
print(alter)

print()

eins = 1                #wenn ohne "" dann ist es ein integer --> für alle zahlen
print(5 * eins)             

print()

eins = "1"              #mit "" ist es ein string, man kann damit nd rechnen
print(5 * eins)

print()

wahre_aussage = True        #booleans sind wahr oder falsch--> Wahrheistwerte
falsche_aussage = False

print()

################ jetzt turtle bibliothek feld größe -200 bis 200 hoch und runter

forward(100)                        #100 pixel nach vorne
right(90)                           #90 nach rechts
forward(100)
right(90)                          
forward(100)
right(90)                           
forward(100)

goto(100,100)                       #geht direkt zu dieser koordinate
penup()                             #nichts wird mehr gezeichnet
goto(0, -100)                       
pendown()                           #pen runter und dann zeichnet wieder
forward(100)

shape("turtle")                     #ändert die form die es zeichnet
    
##register_shape("schiff", ((0,10), (5,0), (15,0) (20,10)))         #so erstellt man eigene formen die sachen zeichnen
##shape("schiff")

pencolor("orange")          #ändert die stift farbe
forward(100)

bgcolor("black")           #ändert die hintergrundfarbe

fillcolor("orange")        #füllt das gezeichnete aus mit der farbe
begin_fill()                #startet zu füllen alles was danach kommt
forward(100)
right(90)
forward(100)
end_fill()                  #endet mit dem füllen

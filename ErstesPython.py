

### Woche 3
from turtle import *



##aktuelle_position = position()
##print(aktuelle_position)                #gibt die aktuelle position aus der türtle



def baum():                             #erstellen einer definitioon die alles ausführt das darinne steht, wenn diese aufgerufen wird
    setheading(90)
    forward(30)
    left(90)
    forward(30)
    right(120)
    forward(60)
    right(120)
    forward(60)
    right(120)
    forward(30)
    return(aktuelle_position)           #zeichnung geht zurück zum gespeicherten anfang


##aktuelle_position = baum()
##print(aktuelle_position) 



##baum()                                  #so wird eine definition ausgeführt
##baum()                                  #das geht auch zweimal


print()


def baum(x,y):                             #definitionen können auch mit parameter angegeben werden
    up()
    goto(x,y)
    down()
    setheading(90)
    forward(30)
    left(90)
    forward(30)
    right(120)
    forward(60)
    right(120)
    forward(60)
    right(120)
    forward(30)

##baum(-100,-100)                         #parameter müssen dann auch angegeben werden
##baum(70,70)

print()


##for i in [-120, -50, 20, 90]:           #das kann man auch alles in einer for schleife verknüpfen
##    baum(i, 0)


print()


attraktion = ["Big Ben", "Buckingham Palace", "Deine Mama"]


def startet_mit_b(attraktion):                            #def für ausgeben wenn ein string mit b anfängt
    ergebnis = attraktion[0] == "B", "D", "X"            #B kann auch mit einem int verwendet werden, indem mehr buchstavben drinne sind etc
    return ergebnis

big_ben = startet_mit_b("Big Ben")                    #überprüfe, wenn ja sag true
print(big_ben)
print(startet_mit_b("London Eye"))                     #wenn nein dann false
    

print()


def attraktionen_mit_b(liste):                        #def filtert aus attraktionen alles mit b
    ergebnis = []
    for attraktion in liste:
        if startet_mit_b(attraktion):
            ergebnis.append(attraktion)
    return ergebnis

print(attraktionen_mit_b(attraktion))

print()

wohnorte = {                        #dictionaries   Simon ist key und berlin ist value
    "Simon":"Berlin",
    "Stella":"Kiel"
    }

print(wohnorte)                     #ausgabe kann verschueden sein

print()

anzahl = len(wohnorte)              #gibt an was alles im dictionarie ist
print(anzahl)

print()

print("Simon wohnt in", wohnorte["Simon"])      #Man kann das dictionarie auch zugreifen lassen wie listen

print()

wohnorte["Stella"] = "Bremen"                   #eingetragene werte kann man auch ändern
print(wohnorte)

print()

wohnorte["Paul"] = "Potsdam"                    #hinzufgügen von daten in die diktionarie
print(wohnorte)

print()

del(wohnorte["Simon"])                          #löschen von eintragungen
print(wohnorte)

print()

for schluessel in wohnorte.keys():              #um sich alle keys anzeigen zu lassen
    print(schluessel)

print()

for wert in wohnorte.values():              #um sich alle values anzeigen zu lassen
    print(wert)

print()

for paar in wohnorte.items():              #mit . items wird die ganze dictionarie ausgegeben
    print(paar)

print()

for paar in wohnorte.items():                 #mit . items kann man auch auf einzelne schlüssel zugreifen
    print(paar[0], "wohnt in", paar[1])

print()

from random import *           #bibliothek wird hinzugefügt

zahl = random()                     #zahl ist random
print(zahl)

print()

x = randint(1, 6)               #eine random zahl zwischen 1 und 6 wird ausgegeben
print(x)

print()

anzahl = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}         #dictionari zwischen 1 und 6
for i in range(600):                            #600 malgewürfelt
    x = randint(1, 6)
    anzahl[x] = anzahl[x] + 1                   #erhöht den gewürfelten betrag

print(anzahl)

print()



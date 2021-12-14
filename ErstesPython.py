

########### Woche 2

alter = 13
if alter > 10:                                  #if verweigung, wenn das stimmt dann führe das aus, was eingerückt ist,,doppeltpunkte nicht vergessen
    print("Du bist über 10 nice")               #das wird ausgegeben wenn if stimmt
else:
    print("Du bist unter 10")                   #wenn if nicht erfüllt wird, wird else ausgegeben


print()                                         #wenns danach wieder normal steht ist von if befreit


sitze = 1
if sitze == 4:
    print("der tisch is super")
elif sitze < 4:                                 #elif kann fallunterschiede kombinieren, elif kann es beliebig oft geben
    ("der tisch is zu klein")
else:
    print("der tisch is zu gross")


print()


print("a" < "b")                    #wird nach alpahebt genommen a ist kleiner als b weil b nach a kommt
print("a" > "b")
print(6 == 7)                       #heißt == gleich und != ungleich
print(6 != 7)


print()


sitze = 4
ort = "Fenster"
if sitze == 4 and ort == "Fenster":                 #and is ein boolean, damit lässt sich in eine if o.ä mehrere bedinungen verknüpfen, gibt nur aus wenn beide wahr sind = and/
    print("Nice am Fenster sind 4 Plätze")


print()


if ort == "Fenster" or ort == "Tür":                #or, da muss nur mind. einer der aussagen richtig sein. 
    print("Der Tisch ist am Fenster oder Tür")


print()


if sitze == 4 and ort == "Fenster" or ort == "Tür":      #kombination mehrer Faktoren, wenn eine in Klammern wird die zuerst gefragt and (ort ...)-
    print("den tisch nehmen wir")
elif sitze != 4:
    print("Wir brauchen genau 4 Plätze")
else:
    print("da fehlt was")


print()


for wort in ("bald", "gibt", "es", "essen"):
    print(wort)


print()


for zahl in (0, 1, 2, 3, 4, 5):                     #widerholt die schritte bis alle abgearbeitet sind
    print(zahl)


print()


for zahl in range(6):                              #macht das gleiche aber ohne zahlen zu schreiben mit range
    print(zahl)



print()


summe = 0
for alter in (7, 11, 13, 15, 12):               #man kann auch rechnen lassen
    summe = summe + alter
print(summe)


print()


##from turtle import *
##for a in range(9):                          #einfacher malen
##    forward(100)
##    right(160)


print()


zeit = 40
while zeit >= 15:                           #while schleife führt das aus bis es nemme geht
    print("wir können noch spielen")
    zeit = zeit - 15
    print("wir haben noch ", zeit) 
print("Jetzt gibts essen")


print()


schnitzeljagd = ["Stift", "Regenjacke", "Stift", "Leons Mum"]           #erstellt eine liste, ermöglicht mehrere sachen zusammen zu stellen, sachen können mehrfach vorkommen
print(schnitzeljagd)

print()

anzahl_elemente = len(schnitzeljagd)
print(anzahl_elemente)                                                  #gibt an wiviele sachen in der liste drinne sind

print()

print(schnitzeljagd[0])                                                 #gibt des erste aus dem array an     
print(schnitzeljagd[-1])                                                #bei - fängt es hinten an

print()

schnitzeljagd[1] = "Schere"                                              #aus der liste kann man einige sachen ersetzen
print(schnitzeljagd[1])

print(schnitzeljagd[0][1])                                              #doppelte indexierung, nimmt den ersten arry und zweite buchstabe

schnitzeljagd = "Stift"
print(schnitzeljagd[2])                                                 #bei keiner lsite gibt es den zweiten buchstaben des strings an, bei int geht das nicht


print()

schnitzeljagd = ["Simon", "Leonie"]
in_schule = ["Stella"]
print(schnitzeljagd + in_schule)                                                #listen kann man auch addieren     oder multi etc
print(schnitzeljagd * 2)    


print()


schnitzeljagd = ["Simon", "Leonie"]
schnitzeljagd.append("Stefan")                                            #fügt am ende der liste sachen hínzu
print(schnitzeljagd)

print()


schnitzeljagd.pop()                                                         #bei pop wird in der klammerderinzex angegeben wenn pop(0) wird das erste entfernt
print(schnitzeljagd)                                                        #so entfernt man die letze eintrag


print()


schloss_mit_code = ["rot", [1, 8]]                                          #man kann auch string und int zussamen reinschreiben wobei [] ein neuer array ist
print(schloss_mit_code[0][0])
print(schloss_mit_code[1][1])

print(schloss_mit_code [0:2] )                                                  #mit : kann man bis zu einem bestimmtgen punkt sich das array auslesen lassen

print()

satz = "Simon und Leonie sind auf Schnitzeljagd"
geteilter_satz = satz.split()                                                   #mit split werden alle teile geteilt, man kann aber auch nur einzelne teile behalten
print(geteilter_satz)                                                        #einzelne sachen kann man sich speichern mit []

print()

satz = ['Simon', 'und', 'Leonie', 'sind', 'auf', 'Schnitzeljagd']
verbundener_satz = " ".join(satz)                                                       #die zerhakten sachen werden zueinadner gefügt und ein Leehrzeichen hinterlassen
print(verbundener_satz)

print()

satz = ['Simon', 'und', 'Leonie', 'sind', 'auf', 'Schnitzeljagd']
for hinweise in satz:                                                                   #gibt nacheinander alles aus
    print(hinweise)

print()

satz = ['Der', 'und', 'rechte', 'sind', 'Weg', 'Schnitzeljagd']
for hinweise in satz:                                                                   
    if hinweise[1] == "e":                                                              #geht auch mit if um einzelne sahcne herauszufiltern
        print(hinweise)


print()
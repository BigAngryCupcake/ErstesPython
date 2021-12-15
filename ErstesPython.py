

### Woche 4


try:                                                                    #try dient abfangen von fehlern, der folgdende text wird versucht
    anzahl_bisher = 10
    anzahl = int(input("Wieviele seid ihr? "))                          #input, für eingabe mit tastatutr, int wandelt den string in einen int um, float in einen float
    print(f"Insgesamt sind wir {anzahl_bisher + anzahl}. ")             #gibt text aus und addiert dei int
except ValueError:                                                      #wenn ValueError vorkommt, dann gibt er folgende befehle aus
    print("Duuuu doofi bitte in Zahlen angeben")        

print()

from random import randint
zahl = randint(1, 100)                                                      #es wird sich eine random zahl ausgedacht
gefunden = False 
print("Ich habe mir eine Zahl ausgedacht")



while gefunden == False:                                                    ##while zum überprüfen bis es gefunden ist
        
    eingabe = input("Gib eine Zahl zwischen 1 und 100 ein ")                 #man gibt eine zahl ein und versucht die vom pc zu finden
    print()
    try:
        eingabe_zahl = int(eingabe)                                         #zahl wird zu int
        if eingabe_zahl == zahl:                                            #zahl wird überprüft
             print("Das war meine Zahl wuhu")
             print()
             gefunden = True
        elif eingabe_zahl < zahl:                                           #wenn zahl kleiner is
            print(f"{eingabe_zahl} war leider zu klein")   
            print()
        else:                                                               #wenn zahl größer is
            print(f"{eingabe_zahl} war leider zu groß")
            print()

    except ValueError:                                                      #wenn value error
        print("Das war keine gültige Eingabe") 
        print() 

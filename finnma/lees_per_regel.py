# Bestand in read-only (r) mode openen (wel zo veilig, we gaan niets overschrijven)
bestand = open("klasgenoten.txt", "r")

# Een tekst naar het bestand schrijven
regel1 = bestand.readline()
print(regel1)

regel2 = bestand.readline()
print(regel2)

regel3 = bestand.readline()
print(regel3)

# Enzovoorts

# Bestand in read-only (r) mode openen (wel zo veilig, wegaan niets schrijven)
bestand = open("klasgenoten.txt", "r")

# Eerste regel inlezen en opslaan in de variabele: tekst_regel
tekst_regel = bestand.readline()

# while loop gaat door zolang er iets in de variabele tekst_regel staat
while tekst_regel:
    # Let op: laat de code in de while loop 4 spaties inspringen!

    # De regel op het scherm zetten:
    print(tekst_regel)

    # Volgende regel ophalen, zodat de while loop doorgaat
    tekst_regel = bestand.readline()

import os

# Bestandsnaam in variabele zetten
bestandsnaam = "demobestand.txt"

# Vraag de huidige map op en sla op in variabele: huidige_map
huidige_map = os.getcwd()

# met de os.path module kun je paden naar bestanden samenstellen
volledige_pad = os.path.join(huidige_map, bestandsnaam)
print("Dit bestand gaan we hernoemen: " + volledige_pad)

# Om nieuwe naam vragen
nieuwe_naam = input("Nieuwe bestandsnaam: ")

if len(nieuwe_naam) > 0:
    # Map en nieuwe bestandsnaam gebruiken om volledige pad samen te stellen
    nieuwe_volledige_pad = os.path.join(huidige_map, nieuwe_naam)
    print("Bestand wordt hernoemd naar: " + volledige_nieuwe_pad)

    # Bestand hernoemen 
    os.rename(volledige_pad, nieuwe_volledige_pad)
    print("Bestand hernoemd")
else:
    print("Sorry, geen geldige invoer, einde programma")

    import os

# Vragen om het bestand
bestand = input("Welk bestand wil je verwijderen? ")

if len(bestand) > 0:
    # controleren of dit bestand wel bestaat met os.path.exists()
    if os.path.exists(bestand):
        # Bestand verwijderen
        os.remove(bestand)
        print("Het bestand " + bestand + " is verwijderd. Jammer dan.")
    else:
        print("Dit bestand bestaat niet, sorry.")
else:
    print("Geen invoer, script zal stoppen")

    import os

# Huidige map opslaan in variable: huidige_map
huidige_map = os.getcwd()

# De os.scandir() functie leest ALLE mappen en bestanden en zet ze in een list
# De list wordt hier opgeslagen in de variabele: alle_bestanden,
alle_bestanden = os.scandir(huidige_map)

# Met een for loop en print() kun je alles uit de list op het scherm zetten
print("Inhoudsopgave van de map: " + huidige_map)


for bestand in alle_bestanden:    
    if bestand.is_file():
        # Dit wordt uitgevoerd als dit een normale file is
        print(bestand.name + " (BESTAND)")
    elif bestand.is_dir():
        # Dit wordt uitgevoerd als dit een dir(ectory) is
        print(bestand.name + " (MAP)")
    else:
        # Dit wordt uitgeveord als het geen file en geen dir is
        print(bestand.name + " (ONBEKEND TYPE")

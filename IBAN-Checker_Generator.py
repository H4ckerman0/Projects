from requests import get
from random import randint,choice

def check_DE_IBAN(IBAN,dateiname):
    blz_liste = []
    address_list = []
    DE = "131400"
    ländercode = IBAN[:2]
    prüfzahl = IBAN[2:4]
    blz = IBAN[4:12]
    kontonummer = IBAN[12:].zfill(10)
    echte_prüfzahl = str(98 - int(blz + kontonummer + DE) % 97).zfill(2)

    with open(dateiname,"r") as datei:
        datei = datei.read()
        datei = datei.splitlines()

        for zeile in datei:
            blz_liste.append(zeile[:8])
            address_list.append(zeile[9:-34])
    
    if blz in blz_liste and ländercode == "DE":
        address = address_list[blz_liste.index(blz)]
    
    else:
        return "Die BLZ ist entweder falsch oder die IBAN ist nicht in Deutschland zufinden. Probieren sie es noch einmal."

    if prüfzahl == echte_prüfzahl:
        return f"IBAN: {IBAN}, Bank-Adresse: {' '.join(address.split())}"

    else: 
        return "Die IBAN hat keine gültige Prüfzahl."

def download_datei(url,dateiname="blz.txt"):
    with open(dateiname,"wb") as datei:
        antwort = get(url)
        datei.write(antwort.content)
    return dateiname

def generiere_IBAN(dateiname):
    blz_liste = []
    DE = "131400"
    kontonummer = str(randint(0,9999999999)).zfill(10)

    with open(dateiname,"r") as datei:
        datei = datei.read()
        datei = datei.splitlines()

        for zeile in datei:
            blz_liste.append(zeile[:8])

    blz = choice(blz_liste)

    prüfzahl = str(98 - int(blz + kontonummer + DE) % 97).zfill(2)  # Prüfzahl-Funktion

    IBAN = "DE" + prüfzahl + blz + kontonummer

    return IBAN

if __name__ == "__main__":
    # Datei mit aktuellen daten bezüglich der Banken in Deutschland und ihrer Bankleitzahl (BLZ)
    dateiname = download_datei("https://www.bundesbank.de/resource/blob/602632/99620ad6ef09483325afa9299450a688/mL/blz-aktuell-txt-data.txt")
    generierte_IBAN = generiere_IBAN(dateiname) # Generiert UND prüft auf Gültigkeit (korrekte prüfzahl und BLZ in Deutschland)
    
    user_input = input("\nWollen sie eine IBAN generieren lassen (a)\noder ihre IBAN prüfen lassen (b)?\n(Geben sie den jeweiligen Buchstaben ein): ")
    print("")

    # Generieren UND Zur Sicherheit prüfen
    if user_input.lower() == "a":
        print(check_DE_IBAN(generierte_IBAN,dateiname))

    # Auf Gültigkeit prüfen (korrekte prüfzahl und BLZ in Deutschland)
    elif user_input.lower() == "b":
        user_IBAN = input("Geben sie die zu prüfende IBAN ein: ")
        print(check_DE_IBAN(user_IBAN,dateiname))

    else: print("Ungültige Eingabe.")
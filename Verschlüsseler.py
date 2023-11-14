import os

answer = input("\nGeben sie den Pfad des Verzeichnis ein (Verzeichnis mit wenig Dateien empfohlen, da zu jeder Datei drei weitere generiert werden): ")
path = answer
size = 0

# Verschlüsseln
def encrypt(file):

    with open(file, "rb") as f:
        f = f.read()
        length = len(f)
        key = os.urandom(length)    # Schlüssel generieren

    with open(f"{file}.key", "wb") as f_key:
        f_key.write(key)                        # Schlüssel-datei generieren (1. Datei)
    
    with open(f"{file}.crypt", "wb") as f_crypt:

        # One-Time-Pad Verschlüsselung
        f_crypt.write(bytes([a^b for a,b in zip(f,key)]))   # Verschlüsselte Datei mit Schlüssel generieren (2. Datei)

# Entschlüsseln
def decrypt(file):
    path_split = file.split("/")
    filename = path_split[-1]
    path_split[-1] = f"decrypted_{filename}"
    decrypt_path = "/".join(path_split)

    with open(f"{file}.crypt", "rb") as f:
        crypt = f.read()                        # Verschlüsselte Datei auslesen                       

    with open(f"{file}.key", "rb") as f:
        key = f.read()                          # Schlüssel-datei auslesen

    with open(decrypt_path, "wb") as file:
        file.write(bytes([a^b for a,b in zip(crypt,key)]))  # Verschlüsselte Datei mit Schlüssel in eine Datei entschlüsseln (3. Datei)

# Verzeichnis durchlaufen und Größe des Verzeichnis in Bytes berechnen
for files in os.walk(path):

    for file in files[2]:
        directory = files[0]
        if "\\" in directory:
            directory = directory.replace("\\","/")

        file_path = f"{directory}/{file}"
        size += os.path.getsize(file_path)

# Erforderliche Größe berechnen
while (answer := input(f"Möchten sie wirklich das gesamte Verzeichnis verschlüsseln (Speicherplatz erforderlich: {size*4/1000000}MB) (ja/nein)? ")) not in ["ja","nein"]:
    print("Ungültige Antwort!")

if answer == "ja":
    
    # Verzeichnis durchlaufen und jede Datei mit unterschiedlichen Schlüssel verschlüsseln und entschlüsseln
    for files in os.walk(path):

        for file in files[2]:
            directory = files[0]
            if "\\" in directory:
                directory = directory.replace("\\","/")

            file_path = f"{directory}/{file}"
            size += os.path.getsize(file_path)
            encrypt(file_path)
            decrypt(file_path)

elif answer == "nein":
    print("Alles klar!")



import string as s
import secrets,random,re

def password_generate(length):
    small,big,digit,punct = s.ascii_lowercase,s.ascii_uppercase,s.digits,s.punctuation
    characters = [small,big,digit,punct]
    password = []

    for char in characters:
        password.append(secrets.choice(char))
        password.append(secrets.choice(char))

    while len(password) < length:
        if len(re.findall("\d","".join(password))) >= int(length*0.7) and digit in characters:  # Verhindert, dass über 70% des Passworts aus Zahlen besteht
            characters.remove(digit)
            print("REMOVED")
        password.append(secrets.choice("".join(characters)))    # Fügt neue Zeichen in das Passwort rein, bis die gewünschte Länge erreicht ist

    random.shuffle(password)
    
    while len(password) > length:   # Verhindert, dass das Passwort länger als gewünscht ist
        password.pop()

    while re.findall("\d\d\d+","".join(password)):  # Verhindert das mehr als drei Zahlen im Passwort hintereinander vorkommen
        random.shuffle(password)

    return "".join(password)    # Finales Passwort

if __name__ == "__main__":
    while (length := int(input("\nWie lang soll ihr sicheres Passwort sein (mind. 20)? "))) > 20:
        print("Ihr Passwort ist zu lang (mind. 20)!")

    password = password_generate(length)
    print(password)
import hashlib, itertools, random, os
import string as s
from Passwort_Generator import password_generate

letter,digit,punct = s.ascii_letters,s.digits,s.punctuation
characters = letter + digit + punct

def calc_hashval(text):
    sha1_val = hashlib.sha1(text)
    hex_hash_val = sha1_val.hexdigest()
    return hex_hash_val

# systematic approach (Geht jedes mögliche Passwort mit einer Länge von 6-10 Zeichen durch)
def crack_password_systematically(hashval,min=6,max=10):   # ~66.000 years
    for l in range(min,max+1):
        for password in itertools.product(characters,repeat=l):
            password = "".join(password)
            password_hash = calc_hashval(password.encode())

            if password_hash == hashval:
                return password
    print(f"Das Passwort ist länger {max} oder kleiner als {min} Zeichen lang!")

# random approach (Generiert Zufällige Passwörter bis er das richtige generiert)
def crack_password_randomly(hashval,min=6,max=10):  # every password has an 1 in 54.440.667.438.733.198.016 chance

    while True:
        length = random.randint(min,max)
        password = password_generate(length)

        password_hash = calc_hashval(password.encode())

        if password_hash == hashval:
            return password

# Geht jede am häufigste verwendete Passwörter durch (mit der Passwort liste (rockyou.txt))
def crack_password_with_list(hashval,password_list): # only passwords in passwordlist
    with open(password_list,"rb") as file:
        for password in file:
            password = password.strip()
            password_hash = calc_hashval(password)

            if password_hash == hashval:
                return password.decode()
        print("Passwort ist nicht in der Passwortliste!")

if __name__ == "__main__":

    # Passwort, dass gecrackt wird (geeignetes Beispiel, damit es nicht zu lange dauert: "aaaaaa")
    hash_val = calc_hashval("aaaaaa".encode())

    # Verschiedene Methodenn (Wählen sie aus):

    cracked_password = crack_password_with_list(hash_val, os.path.dirname(__file__) + r"\rockyou.txt")
    #cracked_password = crack_password_systematically(hash_val)
    #cracked_password = crack_password_randomly(hash_val)

    if cracked_password: print(f"Das Passwort ist {cracked_password}!")




















































































































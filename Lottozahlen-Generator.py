import random

if __name__ == "__main__":
    lose = True
    count = 0
    answers = ["y", "n"]
    
    # Lotto-Zahlen generieren
    lotto_numbers = random.sample(range(1,50),6)
    super_number = random.randint(0,9)

    print(f"\nLotto-Zahlen: {lotto_numbers}\nSuper-Zahl: {super_number}")
    while (answer := input("Möchten sie das Programm laufen lassen, um die generierten Lotto-Zahlen zu erraten (y/n)? ")).lower() not in answers:
        print("Ungültige Eingabe")

    if answer == "y":
        
        # Lotto-Zahlen erraten    
        while lose: 
            count += 1

            # user's draw
            user_draw = random.sample(range(1,50),6)
            user_super_number = random.randint(0,9)
            print(f"\nDeine Ziehung: {user_draw}\nDeine Super-Zahl: {user_super_number}")

            print(f"\nLotto-Zahlen: {lotto_numbers}\nSuper-Zahl: {super_number}")

            # equality check
            if set(user_draw) == set(lotto_numbers) and user_super_number == super_number:
                lose = False    #loop-break
                print("Du hast gewonnen!\n")
            else:
                print(f"Du hast leider keinen Hauptgewinn. {count}\n")

    elif answer == "n":
        print("Alles klar!")
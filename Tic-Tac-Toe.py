from random import randint

# Bitte im Terminal oder in der CMD ausführen.

field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

player = "O"

def display(matrix):
    result = "\n  y 1   2   3\nx\n"
    y = 1
    for row in matrix:
        result += f"{str(y)}  "
        y += 1
        for col in row:
            result += f" {col} |"
        result = result[:-1]
        result += "\n   -----------\n"
    result = result[0:-13]
    print(result)

def check_winner(matrix,player):
    state = check_state(matrix)
    if state == 1:
        print(f"\n{player} gewinnt!")
        quit()

    if state == 0:
        print("\nUnentschieden!")
        quit()

    if state == -1:
        print(f"\n{player} gewinnt!")
        quit()

def check_state(matrix):
    column = [list(i) for i in zip(*matrix)]
    diagonal1 = [matrix[i][i] for i in range(3)] 
    diagonal2 = [matrix[i][-i-1] for i in range(3)]
    state = None
    for row in matrix:
        if len(set(row)) == 1 and not " " in row:
            if row[0] == "O": state = 1
            elif row[0] == "X": state = -1

    for col in column:
        if len(set(col)) == 1 and not " " in col:
            if col[0] == "O": state = 1
            elif col[0] == "X": state = -1

    if len(set(diagonal1)) == 1 and not " " in diagonal1:
        if diagonal1[0] == "O": state = 1
        elif diagonal1[0] == "X": state = -1

    if len(set(diagonal2)) == 1 and not " " in diagonal2:
        if diagonal2[0] == "O": state = 1
        elif diagonal2[0] == "X": state = -1

    if " " not in [e for row in matrix for e in row]:
        state = 0

    return state


def max(matrix):
    best_state = -100

    if check_state(matrix) == 1:
        return 1
    elif check_state(matrix) == 0:
        return 0
    elif check_state(matrix) == -1:
        return -1

    for x,row in enumerate(matrix):
        for y,col in enumerate(row):
            if col == " ":
                matrix[x][y] = "O"

                state = min(matrix)

                if state > best_state:
                    best_state = state

                matrix[x][y] = " "

                return best_state
                
def min(matrix):
    best_state = 100

    if check_state(matrix) == 1:
        return 1
    elif check_state(matrix) == 0:
        return 0
    elif check_state(matrix) == -1:
        return -1

    for x,row in enumerate(matrix):
        for y,col in enumerate(row):
            if col == " ":
                matrix[x][y] = "X"

                state = max(matrix)

                if state < best_state:
                    best_state = state

                matrix[x][y] = " "

                return best_state

def bot_place(matrix):
    best_state = 100
    for x,row in enumerate(matrix):
        for y,col in enumerate(row):
            if col == " ":
                matrix[x][y] = "X"
                if check_state(matrix) == -1:
                    return

                state = max(matrix)
                if state < best_state:
                    best_state = state
                    best_pos = x,y
                matrix[x][y] = " "
    matrix[best_pos[0]][best_pos[1]] = "X"

def place_char(matrix,player,x,y,is_bot=False):
    x -= 1
    y -= 1
    if x > 2:x = 2
    if y > 2:y = 2

    while matrix[x][y] != " ":
        if is_bot:
            x,y = randint(0,2),randint(0,2)

        else:
            print("Da kannst du dein Stein nicht platzieren! Nochmal!")
            answer = input(f"Spieler {player} ist dran: ")

            x = int(answer[0]) - 1
            y = int(answer[1]) - 1

        if x > 2:x = 2
        if y > 2:y = 2

    matrix[x][y] = player

with_bot = input("Willst du gegen einen Bot spielen (ja/nein)? ")
with_bot = with_bot.strip()

while with_bot not in ["ja", "nein"]:
    print("Ungültige Antwort")
    with_bot = input("Willst du gegen einen Bot spielen (ja/nein)? ")

if with_bot == "ja":

    difficulty = input("Wie schwer soll der Bot sein (leicht/schwer)? ")
    difficulty = difficulty.strip()

    while difficulty not in ["leicht","mittel","schwer"]:
        print("Ungültige Antwort!")
        difficulty = input("Wie schwer soll der Bot sein (leicht/mittel/schwer)? ")

if __name__ == "__main__":

    if with_bot == "ja":
        
        if difficulty == "leicht":

            display(field)

            while True:

                if player == "O":
                    answer = input("Du bist dran: ")

                    while len(answer.strip()) <= 1 or not answer.isnumeric():
                        print("Ungültige Eingebe! Nochmal!")
                        answer = input("Du bist dran: ")
                    
                    place_char(field,player,int(answer[0]),int(answer[1]))
                elif player == "X":
                    place_char(field,player,randint(1,3),randint(1,3),True)

                display(field)
                check_winner(field,player)

                if player == "X": player = "O"
                elif player == "O": player = "X"

        elif difficulty == "mittel":

            display(field)

            while True:

                if player == "O":
                    answer = input("Du bist dran: ")

                    while len(answer.strip()) <= 1 or not answer.isnumeric():
                        print("Ungültige Eingebe! Nochmal!")
                        answer = input("Du bist dran: ")
                    
                    place_char(field,player,int(answer[0]),int(answer[1]))
                elif player == "X":
                    bot_place(field)

                display(field)
                check_winner(field,player)

                if player == "X": player = "O"
                elif player == "O": player = "X"

        elif difficulty == "schwer":
            place_char(field,"X",randint(1,3),randint(1,3),True)

            display(field)

            while True:

                if player == "O":
                    answer = input("Du bist dran: ")

                    while len(answer.strip()) <= 1 or not answer.isnumeric():
                        print("Ungültige Eingebe! Nochmal!")
                        answer = input("Du bist dran: ")
                    
                    place_char(field,player,int(answer[0]),int(answer[1]))
                elif player == "X":
                    bot_place(field)

                display(field)
                check_winner(field,player)

                if player == "X": player = "O"
                elif player == "O": player = "X"

    elif with_bot == "nein":
        
        display(field)

        while True:

            answer = input(f"Spieler {player} ist dran: ")

            while len(answer) <= 1 or not answer.isnumeric():
                print("Ungültige Eingebe! Nochmal!")
                answer = input(f"Spieler {player} ist dran: ")

            place_char(field,player,int(answer[0]),int(answer[1]))

            display(field)
            check_winner(field,player)

            if player == "X": player = "O"
            elif player == "O": player = "X"
            
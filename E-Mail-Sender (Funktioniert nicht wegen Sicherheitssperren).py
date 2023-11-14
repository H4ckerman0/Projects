import smtplib

# EMail-Sender funktioniert NICHT, aufgrund von Sicherheitssperren der E-Mail-Provider

EMAIL_PROVIDER = {
    "gmail.com": {"smtp_server": "smtp.gmail.com","smtp_port": 587},
    "web.de": {"smtp_server": "smtp.web.de","smtp_port": 587},
    "hotmail.com": {"smtp_server": "smtp-mail.outlook.com","smtp_port": 587}
}

def send_email(username,password,sender,receiver,head,message):

    data = f"From:{sender}\nTo:{receiver}\nSubject:{head}\n\n{message}"                 # EMAIL-Message
    provider = sender.split("@")[-1]                                                    
    smtp_adress = EMAIL_PROVIDER[provider]                                              # SMTP-Adresse

    server = smtplib.SMTP(f"{smtp_adress['smtp_server']}:{smtp_adress['smtp_port']}")   # Jeweiliger SMTP-Server

    # Server-Start und Einloggen
    server.starttls()
    server.login(username,password)
    server.sendmail(sender,receiver,data)

    # Server-Stop
    print("E-Mail wurde versendet!")
    server.quit()

# Inputs
username = input("Geben sie ihren E-Mail-Nutzernamen ein: ")
password = input("Geben sie ihren E-Mail-Passwort ein: ")
sender = input("Geben sie ihre E-Mail-Adresse ein: ")
receiver = input("Geben sie die E-Mail-Adresse des Empfängers ein: ")
head = input("Geben sie den Betreff ihrer E-Mail ein: ")
message = input("Geben sie die Nachricht, die sie versenden möchten, ein: ")

# EMail-Sender funktioniert NICHT, aufgrund von Sicherheitssperren der E-Mail-Provider
send_email(username,password,sender,receiver,head,message)
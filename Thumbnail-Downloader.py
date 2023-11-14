from requests import get

def download(url,filename="thumbnail.png"):

    # Gültigkeit der URL prüfen
    while not "www.youtube.com" in url and not "youtu.be" in url:
        print("Dies ist keine YoutTube-URL!")
        url = input("Geben sie eine YoutTube-URL ein: ")

    # Youtube-video-code in variable url speichern
    if "youtu.be" in url: url = url.split("/")[-1]
    elif "www.youtube.com" in url: url = url.split("=")[1][:11]

    # Jeweiliges Thumbnail in höchster Auflösung herunterladen
    request_answer = get(f"https://img.youtube.com/vi/{url}/maxresdefault.jpg")
    with open(filename,"wb") as file:
        file.write(request_answer.content)

    print("Download erfolgreich ausgeführt!")

# Input
url = input("Geben sie eine YoutTube-URL ein: ")
filename = input("Gib einen Datei-Namen (.png) ein (nicht erforderlich): ")

if not filename: download(url)
else: download(url,filename)
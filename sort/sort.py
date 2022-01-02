from pathlib import Path

"""
Trier les fichiers contenus dans le dossier data selon les associations suivantes :
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
"""

"""
1 : récupérer en input, le chemin du dossier à analyser et dans lequel faire le tri
2 : faire la liste des fichiers à trier
3 : identifier les formats de fichiers. Ce sera nécessaire pour savoir quel dossier on doit créer
4 : si dossier de tri inexistant(s), créer le(s) dossier(s)
5 : déplacer les fichiers dans les bons dossiers
"""

path_input = Path(input("Indiquez le chemin du dossier à analyser: "))

def read_file():

    global path_input

    print(path_input)

    for f in path_input.iterdir():
        print(f.name)

if not path_input.exists():
    print("Le chemin indiqué n'existe pas.")

elif path_input.is_file():
    print("Vous devez indiquer un dossier et non un fichier.")

elif path_input.is_dir():
    read_file()
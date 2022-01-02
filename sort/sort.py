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

# get the path from the user
path_input = Path(input("Indiquez le chemin du dossier à analyser: "))

# bool to check folder creation
musiques_folder_created = False
videos_folder_created = False
images_folder_created = False
documents_folder_created = False
divers_folder_created = False


def read_file():

    global musiques_folder_created
    global videos_folder_created
    global images_folder_created
    global documents_folder_created
    global divers_folder_created

    musiques_formats = [
        ".mp3", 
        ".wav",
        ".flac"
    ]

    videos_formats = [
        ".avi",
        ".mp4",
        ".gif"
    ]

    images_formats = [
        ".bmp",
        ".png",
        ".jpg"
    ]

    documents_formats = [
        ".txt",
        ".pptx",
        ".csv",
        ".xls",
        ".odp",
        ".pages"
    ]

    global path_input

    print(path_input)

    for f in path_input.iterdir():

        if f.suffix in musiques_formats:

            if not musiques_folder_created:
                print("Créer le dossier Musiques")
                musiques_folder_created = True

            print(f"{f.name} => Déplacer dans Musiques")

        elif f.suffix in videos_formats:

            if not videos_folder_created:
                print("Créer le dossier Vidéos")
                videos_folder_created = True

            print(f"{f.name} => Déplacer dans Vidéos")

        elif f.suffix in images_formats:

            if not images_folder_created:
                print("Créer le dossier Images")
                images_folder_created = True

            print(f"{f.name} => Déplacer dans Images")

        elif f.suffix in documents_formats:

            if not documents_folder_created:
                print("Créer le dossier Documents")
                documents_folder_created = True

            print(f"{f.name} => Déplacer dans Documents")

        else:

            if not divers_folder_created:
                print("Créer le dossier Divers")
                divers_folder_created = True

            print(f"{f.name} => Déplacer dans Divers")


def create_folder(str):

    global path_input

    path_input_new_folder = path_input / str

    print(path_input_new_folder)

if not path_input.exists():
    print("Le chemin indiqué n'existe pas.")

elif path_input.is_file():
    print("Vous devez indiquer un dossier et non un fichier.")

elif path_input.is_dir():
    read_file()
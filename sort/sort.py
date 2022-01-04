from pathlib import Path

"""
Trier les fichiers contenus dans le dossier data selon les associations suivantes :
mp3, wav, flac : Musiques
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

# var to store folders' names
musiques_folder_name = "Musiques"
videos_folder_name = "Videos"
images_folder_name = "Images"
documents_folder_name = "Documents"
divers_folder_name = "Divers"


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
                print(f"Créer le dossier {musiques_folder_name}")
                musiques_folder_created = True

            print(f"{f.name} => Déplacer dans {musiques_folder_name}")

        elif f.suffix in videos_formats:

            if not videos_folder_created:
                print(f"Créer le dossier {videos_folder_name}")
                videos_folder_created = True

            print(f"{f.name} => Déplacer dans {videos_folder_name}")

        elif f.suffix in images_formats:

            if not images_folder_created:
                print(f"Créer le dossier {images_folder_name}")
                images_folder_created = True

            print(f"{f.name} => Déplacer dans {images_folder_name}")

        elif f.suffix in documents_formats:

            if not documents_folder_created:
                print(f"Créer le dossier {documents_folder_name}")
                documents_folder_created = True

            print(f"{f.name} => Déplacer dans {documents_folder_name}")

        else:

            if not divers_folder_created:
                print(f"Créer le dossier {divers_folder_name}")
                divers_folder_created = True

            print(f"{f.name} => Déplacer dans {divers_folder_name}")


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

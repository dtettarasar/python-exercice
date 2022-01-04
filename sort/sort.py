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

    files_list = [f for f in path_input.iterdir() if f.is_file()]

    print(f"{len(files_list)} fichiers à trier.")

    for f in files_list:

        if f.suffix in musiques_formats:

            print(f"{f.name} => Déplacer dans {musiques_folder_name}")
            folder = get_folder(musiques_folder_name)
            print(f"Chemin : {folder}")
            f.rename(folder / f.name)

        elif f.suffix in videos_formats:

            print(f"{f.name} => Déplacer dans {videos_folder_name}")
            folder = get_folder(videos_folder_name)
            print(f"Chemin : {folder}")
            f.rename(folder / f.name)

        elif f.suffix in images_formats:

            print(f"{f.name} => Déplacer dans {images_folder_name}")
            folder = get_folder(images_folder_name)
            print(f"Chemin : {folder}")
            f.rename(folder / f.name)

        elif f.suffix in documents_formats:

            print(f"{f.name} => Déplacer dans {documents_folder_name}")
            folder = get_folder(documents_folder_name)
            print(f"Chemin : {folder}")
            f.rename(folder / f.name)

        else:

            print(f"{f.name} => Déplacer dans {divers_folder_name}")
            folder = get_folder(divers_folder_name)
            print(f"Chemin : {folder}")
            f.rename(folder / f.name)


def get_folder(folder_name):

    global path_input

    path_input_new_folder = path_input / folder_name

    print(f"Dossier existant ? {path_input_new_folder.exists()}")

    # check if the folder is created
    if not path_input_new_folder.exists():

        # create the path for the new folder
        print(f"Créer le dossier {folder_name}")
        path_input_new_folder.mkdir(exist_ok=True)

    return path_input_new_folder

if not path_input.exists():
    print("Le chemin indiqué n'existe pas.")

elif path_input.is_file():
    print("Vous devez indiquer un dossier et non un fichier.")

elif path_input.is_dir():
    read_file()

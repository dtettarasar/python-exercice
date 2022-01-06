from pathlib import Path

def create_folder(path, folder_dict):
    print("OK")
    print(path)
    print(folder_dict)

# get the path from the user
path_input = Path(input("Indiquez le chemin où créer les dossiers: "))
     
d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

if not path_input.exists():
    print("Le chemin indiqué n'existe pas.")

elif path_input.is_file():
    print("Vous devez indiquer un dossier et non un fichier.")

elif path_input.is_dir():
    create_folder(path_input, d)
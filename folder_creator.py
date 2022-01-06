from pathlib import Path

def create_folder(path, folder_dict):
    print("OK")
    print("Dossiers à créer: ")
    for key in folder_dict:
        
        first_level = path / key
        print(first_level)
        first_level.mkdir(exist_ok=True)
        
        print("Sous dossiers à créer: ")
        for item in folder_dict[key]:
            second_level = first_level / item
            print(second_level)
            second_level.mkdir(exist_ok=True)
        
        print("--------------------")

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
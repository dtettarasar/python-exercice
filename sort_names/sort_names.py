from pathlib import Path

def read_file(file_input):
    content = file_input.read_text().replace('\n', ' ')
    print(content)

# get the path from the user
path_input = Path(input("Indiquez le chemin du fichier txt à analyser: "))

# test the file
if not path_input.exists():
    print("Le chemin indiqué n'existe pas.")

elif path_input.is_dir():
    print("Vous devez indiquer un fichier et non un dossier.")

elif path_input.is_file() and path_input.suffix != ".txt":
    print("Le fichier doit être au format .txt")

else:
    read_file(path_input)


from pathlib import Path

# get the path from the user
path_input = Path(input("Indiquez le chemin du fichier txt à analyser: "))

# print(path_input)

try:
    file_to_read = path_input.read_text()
except:
    print("erreur")
else:
    print(file_to_read)
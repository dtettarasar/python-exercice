from pathlib import Path

def read_file(file_input):
    # clean the text file : replace dot & commas by spaces
    content = file_input.read_text().replace(',', ' ').replace('.', ' ').replace('\n', ' ')
    # delete additional spaces
    content_clean = ' '.join(content.split())
    # convert to list
    content_list = content_clean.split(' ')

    content_list.sort()

    return content_list

# create the text file with clean list names
def write_file(list_to_use):

    output_folder = Path("outputs")

    if not output_folder.exists():
        output_folder.mkdir()

    list_name = "output_list.txt"

    path_output_list = output_folder / list_name

    path_output_list.write_text('\n'.join(list_to_use))

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
    # if file is valid : generate the list and use it to create new text file
    list_names = read_file(path_input)
    write_file(list_names)


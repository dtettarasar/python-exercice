import os
import json

course_list = []

# var pour obtenir la relative path
dirname = os.path.dirname(__file__)
filename_path = os.path.join(dirname, 'course-list.json')


def check_json_file():

    global course_list
    global filename_path

    # print(filename_path)

    check_file_exist = os.path.isfile(filename_path)

    # print(check_file_exist)

    if not check_file_exist:
        with open(filename_path, "w") as f:
            json.dump(list(), f)
    else:
        with open(filename_path, "r") as f:
            course_list = json.load(f)



def display_menu(separator):
    menu_str = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter la liste"""

    global filename_path
    global course_list

    if separator:
        print("")
        print("------------------------")
        print("")
        print(menu_str)
    else:
        print(menu_str)

    choix = input("Votre choix : ")

    if choix == "5":

        with open(filename_path, "w") as f:
            json.dump(course_list, f, indent=4, ensure_ascii=False)

        print("")
        print("A bientôt !")
        return False

    elif choix.isdigit() and int(choix) in range(1,5):

        if choix == "1":
            add_element()
        elif choix == "2":
            remove_element()
        elif choix == "3":
            display_list()
        elif choix == "4":
            empty_list()

    else:
        print("Veuillez saisir une option valide.")
    display_menu(True)

def add_element():
    print("")
    print("Vous avez choisi l'option 1 : Ajouter un élément à la liste.")
    element_to_add = input("Entrez le nom d'un élément à ajouter à la liste : ")
    course_list.append(element_to_add)
    print(f"L'élément {element_to_add} à bien été ajouté à la liste.")

def remove_element():
    print("")
    print("Vous avez choisi l'option 2 : Retirer un élément de la liste.")
    element_to_remove = input("Entrez le nom d'un élément à retirer de la liste : ")
    if element_to_remove in course_list:
        course_list.remove(element_to_remove)
        print(f"L'élément {element_to_remove} à bien été retiré de la liste.")
    else:
        print("Cet élément n'est pas dans la liste.")

def display_list():
    print("")
    print("Vous avez choisi l'option 3 : Afficher la liste.")
    if not course_list:
        print("Votre liste est vide !")
    else:
        print("Voici le contenu de votre liste : ")
        for i, item in enumerate(course_list):
            print(f"{i + 1}. {item}")

def empty_list():
    print("Vous avez choisi l'option 4 : Vider la liste.")
    confirmation_message = """Etes vous sûr de vouloir vider la liste ?
    Tapez "oui" pour confirmer
    Tapez autre chose pour annuler
    """

    if not course_list:
        print("Votre liste est vide !")
        return False

    print(confirmation_message)
    choix = input("Votre choix : ")

    if choix == "oui":
        course_list.clear()
        print("Votre liste a bien été vidée.")
    else:
        return False

check_json_file()

display_menu(False)
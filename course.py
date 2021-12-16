course_list = []

def display_menu(separator):
    menu_str = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter la liste"""

    if separator:
        print("")
        print("------------------------")
        print("")
        print(menu_str)
    else:
        print(menu_str)

    choix = input("Votre choix : ")

    if choix == "5":
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

display_menu(False)
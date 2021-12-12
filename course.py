choix = ""

def display_menu(separator):
    menu_str = """Choisissez parmi les 5 options suivantes : 
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter la liste"""

    if separator:
        print("------------------------")
        print(menu_str)
    else:
        print(menu_str)

display_menu(False)
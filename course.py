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
    
    choix = input("Votre choix : ")

    if choix == "5":
        print("A bientôt !")
    else:
        if choix.isdigit() and int(choix) in range(1,5):
            print("ok")
        else:
            print("Veuillez saisir une option valide")
        display_menu(True)

display_menu(False)
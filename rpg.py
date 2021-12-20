def player_choice():

    choice = ""

    while choice not in ["1", "2"]:
        choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

player_choice()
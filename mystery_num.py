print("--- le jeu du nombre mystère :) ---")

essai = 5
num_to_find = 75

while essai != 0:
    print(f"Il te reste {essai} essai(s)")
    player_num_str = input("Devine le nombre : ")

    if player_num_str.isdigit() == False:
        print("Tu dois entrer un nombre valide.")
    else:

        player_num_int = int(player_num_str)

        if num_to_find < player_num_int:
            print(f"Le nombre mystère est plus petit que {player_num_int}.")
        elif num_to_find > player_num_int:
            print(f"Le nombre mystère est plus grand que {player_num_int}.")
        else:
            print("Bravo!")
            break

        essai -= 1
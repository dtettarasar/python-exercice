import random
print("--- le jeu du nombre mystère :) ---")

essai = const_essai = 5
num_to_find = random.randint(0,100)
# print(f"Random Number : {num_to_find}.")

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
            print(f"Bravo ! Le nombre mystère était bien {player_num_int} !")
            print(f"Tu as trouvé le nombre en {const_essai + 1 - essai} essai(s)")
            print("Fin du jeu.")
            break

        essai -= 1

        if essai == 0:
            print(f"Dommage ! Le nombre mystère était {num_to_find}.")
            print("Fin du jeu.")

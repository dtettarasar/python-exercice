print("--- le jeu du nombre mystère :) ---")

essai = 5
num_to_find = 75

while essai != 0:
    print(f"Il te reste {essai} essai(s)")
    player_num = input("Devine le nombre : ")

    if player_num.isdigit() == False:
        print("Veuillez entrer un nombre valide.")
    else:
        essai -= 1
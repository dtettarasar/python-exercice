import random
player_health = enemy_health = 50
player_rem_potions = 3

def player_choice():

    choice = ""

    while choice not in ["1", "2"]:
        choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

    if choice == "1":
        attack(False)

        if enemy_health == 0:
            print("Vous avez gagné !")
            print("Fin du jeu.")
        elif player_health == 0:
            print("L'ennemi a gagné !")
            print("Fin du jeu.")
        elif player_health == 0 and enemy_health == 0:
            print("Match nul.")
            print("Fin du jeu.")
        else:
            player_choice()

    elif choice == "2":
        use_potion()
        player_choice()

def attack(potion_used):

    global player_health
    global enemy_health

    player_attack = random.randint(5,10)
    enemy_attack = random.randint(5,15)

    if not potion_used:
        enemy_health = enemy_health - player_attack if enemy_health - player_attack > 0 else 0
        print(f"Vous avez infligé {player_attack} points de dégâts à l'ennemi.")

    player_health = player_health - enemy_attack if player_health - enemy_attack > 0 else 0

    if enemy_health != 0:
        print(f"L'ennemi vous a infligé {enemy_attack} points de dégâts.")

    print(f"Vous avez {player_health} point(s) de vie.")
    print(f"L'ennemi a {enemy_health} point(s) de vie.")
    print("--------------------------------")

def use_potion():

    global player_rem_potions
    global player_health
    potion_health = random.randint(15, 50)

    if player_rem_potions != 0:

        if player_health == 50:
            print("Vous disposez déjà de vos 50 points de vie.")

        else:
            player_rem_potions -= 1
            print(f"Vous utilisez une potion : la potion vous donne {potion_health} points de vie.")
            print(f"Il vous reste {player_rem_potions} potions.")
            player_health = player_health + potion_health if player_health + potion_health < 50 else 50

            if player_health == 50:
                print("Vous avez récupéré vos 50 points de vie !")
            else:
                print(f"Vous avez maintenant {player_health} points de vie.")
            attack(True)

            print("Vous passez votre tour...")
            attack(True)

    else:
        print("Vous n'avez plus de potions.")
        print("--------------------------------")


player_choice()
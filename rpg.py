import random
player_health = enemy_health = 50
player_rem_potions = 3

def player_choice():

    choice = ""

    while choice not in ["1", "2"]:
        choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

    if choice == "1":
        attack()
        player_choice()
    elif choice == "2":
        use_potion()
        player_choice()

def attack():

    player_attack = random.randint(5,10)
    enemy_attack = random.randint(5,15)

    print(f"player attack: {player_attack}")
    print(f"enemy attack: {enemy_attack}")
    print("--------------------------------")

def use_potion():
    print("vous utilisez une potion !")
    print("--------------------------------")


player_choice()
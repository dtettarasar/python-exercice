class Voiture():

    essence = 100

    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence}L d'essence")

    def roule(self, km):
        essence_utilise = (km * 5)/100
        if self.essence == 0:
            print("Vous n'avez plus d'essence, faites le plein !")
        elif self.essence < essence_utilise:
            print(f"Vous n'avez pas assez d'essence pour parcourir {km} km, faites le plein !")
        else:
            self.essence -= essence_utilise
            if self.essence < 10:
                print("Vous n'avez bientôt plus d'essence !")
        self.afficher_reservoir()

if __name__ == "__main__":
    print("module voiture.py")
    test_voiture = Voiture()
    print(test_voiture.essence)
    test_voiture.afficher_reservoir()
    for i in range(25):
        test_voiture.roule(85)

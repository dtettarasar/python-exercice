class Voiture():

    essence = 100

    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence}L d'essence")

    def roule(self, km):
        essence_utilise = (km * 5)/100
        self.essence -= essence_utilise
        self.afficher_reservoir()

if __name__ == "__main__":
    print("module voiture.py")
    test_voiture = Voiture()
    print(test_voiture.essence)
    test_voiture.afficher_reservoir()
    for i in range(4):
        test_voiture.roule(25)

class Voiture():

    essence = 100

    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence}L d'essence")

if __name__ == "__main__":
    print("module voiture.py")
    test_voiture = Voiture()
    print(test_voiture.essence)
    test_voiture.afficher_reservoir()

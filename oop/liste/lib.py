class Liste(list):

    def __init__(self, nom):
        self.nom = nom

if __name__ == "__main__":

    test_list = Liste("course")
    print(test_list.nom)
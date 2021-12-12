# get the numbers
number_one = input("Entrez un premier nombre : ")

while number_one.isdigit() == False:
    number_one = input("Veuillez saisir un premier nombre valide : ")

number_two = input("Entrez un deuxième nombre : ")

while number_two.isdigit() == False:
    number_two = input("Veuillez saisir un deuxième nombre valide : ")

final_result = int(number_one) + int(number_two)

final_str = f"Le résultat de l'addition de {number_one} avec {number_two} est égal à {final_result}."

print(final_str)

# get the numbers
number_one = input("enter your first number: ")

while number_one.isdigit() == False:
    number_one = input("Please enter a valid number: ")

number_two = input("enter your second number: ")

while number_two.isdigit() == False:
    number_two = input("Please enter a valid number: ")

final_result = int(number_one) + int(number_two)

final_str = f"The final result is equal to {final_result}"

print(final_str)

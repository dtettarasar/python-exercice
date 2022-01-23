import faker
# print(faker)

# generate one random username
def get_user():

    fake_data = faker.Faker()

    get_f_name = fake_data.first_name()
    get_l_name = fake_data.last_name()

    name_str = f"{get_f_name} {get_l_name}"

    # print("get user function")
    # print(name_str)
    return name_str

# generate a list of random usernames
def get_users(quantity=1):

    name_list = []

    for i in range(quantity):
        name_list.append(get_user())

    return name_list

# Conditions to test functions when executing this module
if __name__ == "__main__":
    user = get_user()
    print(user)

    users_list = get_users(5)
    print(users_list)
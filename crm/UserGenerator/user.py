import faker
# print(faker)

def get_user():

    fake_data = faker.Faker()

    get_f_name = fake_data.first_name()
    get_l_name = fake_data.last_name()

    name_str = f"{get_f_name} {get_l_name}"

    # print("get user function")
    # print(name_str)
    return name_str

def get_users(quantity=1):

    name_list = []

    for i in range(quantity):
        name_list.append(get_user())

    return name_list
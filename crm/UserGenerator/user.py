"""Module to generates random usernames"""
import faker
import logging
from pathlib import Path

base_dir = Path(__file__).resolve().parent
logging.basicConfig(filename=base_dir / "user.log", level=logging.INFO)

def get_user():
    """Generate one random username

    Returns:
        str: username
    """

    logging.info("Generating user.")
    fake_data = faker.Faker()

    get_f_name = fake_data.first_name()
    get_l_name = fake_data.last_name()

    name_str = f"{get_f_name} {get_l_name}"

    # print("get user function")
    # print(name_str)
    return name_str

def get_users(quantity=1):

    """Generate a list of usernames

    Args:
        quantity (int) : number of username to generate

    Returns:
        list[str]: usernames
    """

    logging.info(f"Generating list of {quantity} user(s).")

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
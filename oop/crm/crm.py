import re
import string
class User:
    def __init__(self, first_name: str, last_name: str, phone_number: str="", address: str=""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
    
    def __str__(self):
        return f"User obj:\n{self.full_name}\n{self.phone_number}\n{self.address}"
    
    def __repr__(self):
        return f"User({self.first_name}, {self.last_name})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def _check_phone_number(self):
        phone_number = re.sub(r"[+()\s]*", "", self.phone_number)
        # print(phone_digits)

        if len(phone_number) < 10 or not phone_number.isdigit():
            raise ValueError(f"Following phone number not valid: {self.phone_number}")
    
    def _check_names(self):
        if not (self.first_name and self.last_name):
            raise ValueError("Missing names")
        
        spec_chars = string.punctuation + string.digits

        for char in self.first_name + self.last_name:
            if char in spec_chars:
                raise ValueError(f"Following name not valid: {self.full_name}")
    
    def _checks(self):
        self._check_phone_number()
        self._check_names()

if __name__ == "__main__":
    from faker import Faker
    fake = Faker(locale="fr_FR")
    print("User class module")
    print("-" * 15)

    for _ in range(4):
        user = User(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            phone_number = fake.phone_number(),
            address = fake.address())
        print(user)
        # print(repr(user))
        user._checks()
        print("-" * 15)

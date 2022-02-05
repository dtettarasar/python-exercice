import json
import logging
import os

from constants import DATA_DIR

LOGGER = logging.getLogger()

class List_obj(list):

    def __init__(self, name):
        self.name = name

    def add_element(self, element):

        if not isinstance(element, str):
            LOGGER.error("You can only add strings")
            return False

        if element in self:
            LOGGER.error(f"The element {element} is already in the list")
            return False
        else:
            self.append(element)
            return True

    def remove_element(self, element):

        if element in self:
            self.remove(element)
            return True

        return False

    def display_list(self):
        print(f'content of the list "{self.name}":')

        for e in self:
            print(f"- {e}")

    def save_list(self):
        path = os.path.join(DATA_DIR, f"{self.name}.json")
        # print(path)
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        with open(path, "w") as f:
            json.dump(self, f, indent=4)

        return True


if __name__ == "__main__":

    test_list = List_obj("musique")
    test_list.add_element("Square Hammer")
    test_list.add_element("Square Hammer")
    test_list.remove_element("Square Hammer")
    test_list.add_element("Flying Whales")
    test_list.add_element("The Four Horsemen")
    test_list.add_element("Rust In Peace")
    test_list.add_element("Blow Your Trumpets Gabriel")
    test_list.add_element("Freak on a Leash")
    test_list.display_list()
    test_list.save_list()



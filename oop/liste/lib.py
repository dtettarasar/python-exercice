import logging

LOGGER = logging.getLogger()

class List_obj(list):

    def __init__(self, nom):
        self.nom = nom

    def add_element(self, element):

        if not isinstance(element, str):
            LOGGER.error("You can only add strings")

        if element in self:
            LOGGER.error(f"The element {element} is already in the list")
        else:
            self.append(element)


if __name__ == "__main__":

    test_list = List_obj("course")
    print(test_list.nom)

    test_list.add_element(True)
    test_list.add_element(4)
    test_list.add_element("chocolat")

    test_list_2 = List_obj("musique")
    test_list_2.add_element("Square Hammer")
    print(test_list_2)
    test_list_2.add_element("Square Hammer")


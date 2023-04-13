

class Person:
    # class variable
    name = "SuperMario"

    def __init__(self, person_name, residence_place):
        self.name = person_name
        self.residence_place = residence_place

    def get_name(self):
        return self.name

    def get_residence_place(self):
        return self.residence_place

    def disp_attr(self):
        return self.name, self.residence_place







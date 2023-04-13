from inheritance import Person


class Sister(Person):
    name = "WonderWoman"

    # initialiser
    def __init__(self, person_name, residence_place, exam_course):
        # call to # initialiser of the parent class Student
        super().__init__(person_name, residence_place)

        # instance variable
        self.exam_subjects = exam_course

    # instance method
    def get_exam_subjects(self):
        return self.exam_subjects

    def disp_attr(self):
        return self.name, self.residence_place, self.exam_subjects


def main():

    person_1 = Sister("Hello", "some address", "CDAC")
    # print(f" The name and residence details are as follows: {Sister.name}, {Sister.get_residence_place(Person)}")


main()





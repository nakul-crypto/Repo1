

class Employee:
    # class variable
    department_name = "Technology"

    # initialiser
    def __init__(self, emp_id, emp_salary, mgr_id):
        # instance variable
        self.employee_id = emp_id
        self.employee_salary = emp_salary
        self.manager_id = mgr_id
        print(f"{self} was created successfully with values {emp_id},{emp_salary},{mgr_id}")

    # instance methods
    def get_emp_salary(self):
        return self.employee_salary

    def set_emp_salary(self, rcv_salary):
        self.employee_salary = rcv_salary

    def display(self):
        print(self.employee_id, self.employee_salary, self.manager_id)

    # class method
    @classmethod
    def get_department_name(cls, department_name):
        cls.department_name = department_name

    # static method
    # field_expertise() --> just displays some expertise for all my employees
    @staticmethod
    def field_expertise():
        return "1. Programming, 2. Testing & Debugging\n"


# main method which is outside the class
def main():
    print("Employee Database")

    employee_1 = Employee(100, 1000, 1)
    employee_2 = Employee(10, 500, 10)
    Employee.department_name
    Employee.field_expertise()
    Employee.display()


main()




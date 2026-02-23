class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")
class PartTime(Person):
    def __init__(self, name, age, working_hours):
        super().__init__(name, age)
        self.working_hours = working_hours

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Working Hours: {self.working_hours}")
class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.working_hours = working_hours
        self.project_name = project_name

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, "
              f"Employee ID: {self.employee_id}, "
              f"Working Hours: {self.working_hours}, "
              f"Project Name: {self.project_name}")
person1 = Person("Alice", 30)
employee1 = Employee("Bob", 40, "E123")
parttime1 = PartTime("Charlie", 22, 20.5)
consultant1 = Consultant("Diana", 35, "C456", 15.0, "AI Project")
person1.show_details()
employee1.show_details()
parttime1.show_details()
consultant1.show_details()
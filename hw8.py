class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}")
class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, "
              f"Specialization: {self.specialization}")
class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, "
              f"Yoga Style: {self.yoga_style}")
class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}, Role: {self.role}, "
              f"Specialization: {self.specialization}, "
              f"Yoga Style: {self.yoga_style}")
emp1 = Employee("Arun", "Receptionist")
trainer1 = Trainer("Meera", "Trainer", "Strength Training")
yoga1 = YogaInstructor("Ravi", "Yoga Instructor", "Hatha Yoga")
multi1 = MultiTrainer("Sneha", "Senior Trainer", "Cardio", "Vinyasa")
emp1.display()
trainer1.display()
yoga1.display()
multi1.display()
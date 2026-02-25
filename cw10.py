from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year

    def years_on_platform(self):
        return 2025 - self.joining_year

    @abstractmethod
    def get_role(self):
        pass

    def display_info(self):
        print(f"{self.name} is a {self.get_role()} and has been using the platform for {self.years_on_platform()} years.")

class Customer(User):
    def get_role(self):
        return "Customer"

class Vendor(User):
    def get_role(self):
        return "Vendor"

user1 = Customer("Anjana", 2020)
user2 = Vendor("Rahul", 2018)

user1.display_info()
user2.display_info()
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    def account_age(self):
        return 2025 - self.account_year

    @abstractmethod
    def get_role(self):
        pass

class Admin(User):
    def get_role(self):
        return "Admin"

    def __str__(self):
        return f"{self.name} is an Admin user with {self.account_age()} years on the platform."

class Guest(User):
    def get_role(self):
        return "Guest"

    def __str__(self):
        return f"{self.name} is a Guest user with {self.account_age()} years on the platform."

admin_user = Admin("Anjana", 2019)
guest_user = Guest("Rahul", 2022)

print("Role:", admin_user.get_role())
print("Account Age:", admin_user.account_age())
print(admin_user)

print()

print("Role:", guest_user.get_role())
print("Account Age:", guest_user.account_age())
print(guest_user)
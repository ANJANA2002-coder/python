class Account:
    def __init__(self, name, balance):
        self._name = name        
        self._balance = balance  

    def __add__(self, other):
        return self._balance + other._balance

class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05
class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02

if __name__ == "__main__":

    savings = SavingsAccount("Ravi", 10000)
    current = CurrentAccount("Anjali", 15000)

    print("Account Details")
    print("--------------------------")

    print("Name:", savings._name)
    print("Balance:", savings._balance)
    print("Interest (5%):", savings.calculate_interest())
    print("--------------------------")

    print("Name:", current._name)
    print("Balance:", current._balance)
    print("Interest (2%):", current.calculate_interest())
    print("--------------------------")

    total = savings + current
    print("Total Balance:", total)

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        print(f"Balance: {self.__balance}")


acc1 = BankAccount()
acc1.get_balance()
print("=================================")
acc1.withdraw(100)
acc1.deposit(-1000)
acc1.get_balance()
print("=================================")
acc1.withdraw(500)
acc1.get_balance()
print("=================================")
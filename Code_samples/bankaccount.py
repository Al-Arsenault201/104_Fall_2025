class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner               # public attribute
        self.__balance = balance         # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance            # controlled access

acc = BankAccount("Alice", 100)
#print(acc.__balance)  # AttributeError


print(acc.get_balance())

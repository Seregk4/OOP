class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Введите не отрицательное значение")
        elif amount >= self.__balance:
            print("Недостаточно средств")
        else:
            self.__balance -= amount

    def get_balance(self):
        print(self.__balance)

acc = BankAccount(0)

acc.get_balance()

acc.deposit(1000)
acc.get_balance()

acc.withdraw(-1999)
acc.get_balance()

acc.withdraw(1999)
acc.get_balance()

class BankAccount:
    def __init__(self, account_balance=0):
        self.__account_balance = account_balance  # encapsulated attribute

    def deposit(self, amount):
        self.__account_balance += amount
        return f"Deposited {amount}. New balance is: {self.__account_balance}"

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew {amount}. New balance is: {self.__account_balance}"
        else:
            return "Insufficient funds"

    def display_balance(self):
        return f"Your balance is: {self.__account_balance}"



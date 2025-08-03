class BankAccount:
    def __init__(self, account_balance=0):
        self.__account_balance = float(account_balance)

    def deposit(self, amount):
        amount = float(amount)
        self.__account_balance += amount
        return f"Deposited: ${amount:.2f}"

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew: ${amount:.2f}"
        else:
            return "Insufficient funds."

    def display_balance(self):
        return f"Current Balance: ${self.__account_balance:.2f}"

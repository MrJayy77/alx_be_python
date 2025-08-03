class BankAccount:
    def __init__(self, account_balance=0):
        self.__account_balance = account_balance  # encapsulated attribute

    def deposit(self, amount):
<<<<<<< HEAD
        self.__account_balance += amount
        return f"Deposited {amount}. New balance is: {self.__account_balance}"
=======
    self.account_balance += amount
    return f"Deposited {amount}. New balance is: {self.account_balance}"

    
   def withdraw(self, amount):
    if amount <= self.account_balance:
        self.account_balance -= amount
        return f"Withdrew {amount}. New balance is: {self.account_balance}"
    else:
        return "Insufficient funds"

>>>>>>> 844798b908568f5244c74887a3744f7d0ce78b95

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew {amount}. New balance is: {self.__account_balance}"
        else:
            return "Insufficient funds"

    def display_balance(self):
        return f"Your balance is: {self.__account_balance}"



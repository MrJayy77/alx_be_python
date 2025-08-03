class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance 

    def deposit(self, amount):
    self.account_balance += amount
    return f"Deposited {amount}. New balance is: {self.account_balance}"

    
   def withdraw(self, amount):
    if amount <= self.account_balance:
        self.account_balance -= amount
        return f"Withdrew {amount}. New balance is: {self.account_balance}"
    else:
        return "Insufficient funds"



    def display_balance(self):
        print(f"Your balance is: {self.account_balance}")


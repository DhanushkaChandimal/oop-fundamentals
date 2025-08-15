# attribute - public attribute
# _attribute - protected attribute
# __attribute - private attribute

class BankAccount:
    def __init__(self, account_holder, balance, password):
        self.account_holder = account_holder  # Public attribute
        self._balance = balance  # Protected attribute
        self.__password = password  # Private attribute
    
    def get_balance(self, password):
        if password == self.__password:
            return self._balance
        else:
            return "Access denied"

class SavingsAccount(BankAccount):
    def add_interest(self, interest_rate):
        self._balance += self._balance * interest_rate

# Create a bank account with a protected balance and private password
account = BankAccount("Charlie", 5000, "mypassword")
print(account.account_holder) # Output: Charlie
print(account._balance) # Output: 5000 # not recommended
# print(account.__password) # Raises AttributeError

# Accessing balance with the correct password
print(account.get_balance("mypassword")) # Output: 5000
print(account.get_balance("111")) # Output: 5000

# Accessing private attribute via name mangling (not recommended)
print(account._BankAccount__password) # Output: mypassword
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

print("\n===================================\n")



# # Inheritance
# Parent class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def move(self):
        print(f"{self.name} is moving!")

    def attack(self):
        print(f"{self.name} attacks with {self.attack_power} power!")

# Subclass: Warrior
class Warrior(Character):
    def __init__(self, name, health, attack_power, armor):
        super().__init__(name, health, attack_power)  # Call the parent class constructor
        self.armor = armor

    def use_shield(self):
        print(f"{self.name} blocks the attack with a shield!")
    
    def attack(self):
        # Override the parent class method
        print(f"{self.name} slashes with a sword, dealing {self.attack_power} damage!")

# Subclass: Mage
class Mage(Character):
    def __init__(self, name, health, attack_power, mana):
        super().__init__(name, health, attack_power)
        self.mana = mana

    def cast_spell(self):
        print(f"{self.name} casts a powerful spell!")

# Creating instances
warrior = Warrior("Conan", 100, 20, "Iron Armor")
mage = Mage("Gandalf", 80, 25, 100)

# Calling methods
warrior.move()          # Output: Conan is moving!
warrior.attack()        # Output: Conan attacks with 20 power!
warrior.use_shield()    # Output: Conan blocks the attack with a shield!

mage.move()             # Output: Gandalf is moving!
mage.attack()           # Output: Gandalf attacks with 25 power!
mage.cast_spell()       # Output: Gandalf casts a powerful spell!

print("\n===================================\n")



# # Polymorphism
from abc import ABC, abstractmethod
class Character(ABC):
    @abstractmethod 
    def attack(self):
        print("This method should be overridden by subclasses.")

class Warrior(Character):
    def attack(self):
        print("Warrior attacks with a sword!")

class Mage(Character):
    def attack(self):
        print("Mage casts a fireball!")

# class Archer(Character):
    # print("Archer shoots an arrow!") # Error

# Using polymorphism in a function
def perform_attack(character):
    character.attack()  # Calls the correct method based on the object's class

# Cannot instantiate Character directly: 
# character = Character() # Raises TypeError

# Creating instances of different character types
warrior = Warrior()
mage = Mage()
# archer = Archer()

# Using polymorphism
perform_attack(warrior)  # Output: Warrior attacks with a sword!
perform_attack(mage)     # Output: Mage casts a fireball!
# perform_attack(archer)   # Output: Archer shoots an arrow! # Error

print("\n===================================\n")



# # Multiple inheritance
class Flyer:
    def fly(self):
        print("Flying high!")

class Swimmer:
    def swim(self):
        print("Swimming fast!")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")

# Creating an instance of Duck
duck = Duck()
duck.fly()     # Output: Flying high!
duck.swim()    # Output: Swimming fast!
duck.quack()   # Output: Quack!

class Car:
    # Class Attribute
    wheels = 4

    def __init__(self, make, model, year=2025, mileage=0):
        # Instance Attributes
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        
    # Instance method to display car information
    def display_info(self):
        return f"{self.make} {self.model}, Mileage: {self.mileage} miles"

    # Instance method to update the mileage
    def drive(self, miles):
        self.mileage += miles
        return f"Drove {miles} miles. Total mileage is now {self.mileage} miles."

# Creating instances of the Car class
car1 = Car('Toyota', 'Corolla')
car2 = Car('Honda', 'Civic', 2018)

print(car1.wheels)  # Output: 4
print(car1.make)    # Output: Toyota
print(car2.make)    # Output: Honda
print(car1.year)    # Output: Honda
print(car2.year)    # Output: Honda

# Calling instance methods
print(car1.display_info())  # Output: Toyota Corolla, Mileage: 0 miles
print(car1.drive(150))      # Output: Drove 150 miles. Total mileage is now 150 miles
print(car1.display_info())  # Output: Toyota Corolla, Mileage: 150 miles
print(car1.drive(350))      # Output: Drove 150 miles. Total mileage is now 350 miles
print(car1.display_info())  # Output: Toyota Corolla, Mileage: 500 miles



# Challenges
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hi {self.name} welcome..."
    
    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday! You are now {self.age} years old."

person1 = Person("Dhanushka", 19)
print(person1.greet())
print(person1.have_birthday())
print(person1.have_birthday())

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Your new account balance is ${self.balance}"
    
    def withdraw(self, amount):
        if(self.balance > amount):
            self.balance -= amount
            return f"Your new account balance is ${self.balance}"
        return "Insufficient funds."
    
    def get_balance(self):
        return f"Your account balance is ${self.balance}"

acc1 = BankAccount("Dhanushka", 2000)
print(acc1.get_balance())
print(acc1.deposit(3000))
print(acc1.withdraw(10000))
print(acc1.withdraw(100))
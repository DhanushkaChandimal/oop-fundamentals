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
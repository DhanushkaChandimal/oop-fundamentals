class Car:
    # Class Attribute
    wheels = 4

    def __init__(self, make, model, year=2025):
        # Instance Attributes
        self.make = make
        self.model = model
        self.year = year

# Creating instances of the Car class
car1 = Car('Toyota', 'Corolla')
car2 = Car('Honda', 'Civic', 2018)

print(car1.wheels)  # Output: 4
print(car1.make)    # Output: Toyota
print(car2.make)    # Output: Honda
print(car1.year)    # Output: Honda
print(car2.year)    # Output: Honda

class Car:
    # Class Attribute
    wheels = 4

    def __init__(self, make, model):
        # Instance Attributes
        self.make = make
        self.model = model

# Creating instances of the Car class
car1 = Car('Toyota', 'Corolla')
car2 = Car('Honda', 'Civic')

print(car1.wheels)  # Output: 4
print(car1.make)    # Output: Toyota
print(car2.make)    # Output: Honda

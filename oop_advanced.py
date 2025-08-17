# Special Methods: __repr__ and __str__

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"
    
    def __str__(self):
        return f"{self.name}: ${self.price} (Quantity: {self.quantity})"

# Developer view (using __repr__):
p = Product("Laptop", 999.99, 5)
print(repr(p))  # Output: Product(name='Laptop', price=999.99, quantity=5)

# User view (using __str__):
print(p)  # Output: Laptop: $999.99 (Quantity: 5)
print("\n=====================================\n")



# Class Methods: Managing Class-Level Behavior
class Car:
    total_cars = 0  # Class attribute to track the number of cars
    
    def __init__(self, model, year):
        self.model = model
        self.year = year
        Car.total_cars += 1  # Increment class-level counter when a car is created
    
    @classmethod
    def from_csv(cls, csv_data):
        # Alternative constructor to create cars from CSV-like data
        model, year = csv_data.split(',')
        return cls(model, int(year))
    
    @classmethod
    def total_produced(cls):
        return cls.total_cars
    
# Creating instances the regular way:
car1 = Car("Toyota Corolla", 2020)

# Creating an instance using class method:
car2 = Car.from_csv("Honda Accord,2018")

print(Car.total_produced()) # Output: 2
print(car1.total_produced()) # Retrieve using instances
print(car2.total_produced()) # Retrieve using instances
print("\n=====================================\n")



# Static Methods: Utility Functions within Classes
class WeatherStation:
    
    def __init__(self, location, temperature_f):
        self.location = location
        self.temperature_f = temperature_f
    
    def __repr__(self):
        return f"WeatherStation(location={self.location}, temperature_f={self.temperature_f})"
    
    @staticmethod
    def fahrenheit_to_celsius(f_temp):
        return (f_temp - 32) * 5.0/9.0
    
    @staticmethod
    def celsius_to_fahrenheit(c_temp):
        return (c_temp * 9.0/5.0) + 32

# Usage of static methods:
temp_f = 77
temp_c = WeatherStation.fahrenheit_to_celsius(temp_f) #Notice here we didn't make any instance from the class
print(f"{temp_f}F is {temp_c:.2f}C")  # Output: 77F is 25.00C

temp_back_f = WeatherStation.celsius_to_fahrenheit(temp_c)
print(f"{temp_c:.2f}C is {temp_back_f:.2f}F")  # Output: 25.00C is 77.00F
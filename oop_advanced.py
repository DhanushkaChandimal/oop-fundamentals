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
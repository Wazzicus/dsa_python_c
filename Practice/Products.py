class Product:
    def __init__(self, product_name, product_price):
        self.name = product_name
        self.price = product_price

p1 = Product("My first product", 100)
print(p1)
class Product:
    name: str
    description: str
    price: float
    quantity: int
    products = []

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.products.append(name)


class Category:
    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = []

        Category.category_count += 1
        Category.product_count = len(products)

class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Возвращает цену продукта"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Устанавливает новую цену продукта"""
        if new_price >= 0:
            self.__price = new_price
        elif new_price < 0:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

    def add_product(self, product):
        """Счетчик продуктов"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print("Можно добавлять только объекты типа Product")

    @property
    def products(self):
        """Геттер для продуктов"""
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products)

    @classmethod
    def new_product(cls, product_data):
        """Создает новый продукт на основе словаря."""
        return cls(name=product_data['name'], description=product_data['description'], price=product_data['price'],
                       quantity=product_data['quantity'])

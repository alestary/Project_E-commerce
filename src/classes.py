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

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сумма всех товаров на складе"""
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Операнд справа должен иметь тип Product")

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

    @classmethod
    def new_product(cls, product_data):
        """Создает новый продукт на основе словаря."""
        return cls(name=product_data['name'], description=product_data['description'], price=product_data['price'],
                   quantity=product_data['quantity'])


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0
    product_quantity = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

    def __add__(self, other):
        if isinstance(other, Product):
            self.__products.append(other)
            Category.product_count += 1
        else:
            return "Можно добавлять только объекты типа Product"

    def add_product(self, product):
        """Счетчик продуктов"""
        Category.__add__(self, product)
        self.product_quantity += product.quantity
        return self.product_quantity

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_quantity} шт."

    def get_products(self):
        return self.__products

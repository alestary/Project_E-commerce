from abc import ABC, abstractmethod


class CreationInfoMixin:
    def __init__(self, *args, **kwargs):
        print(f"Создан объект класса {self.__class__.__name__} с параметрами: {args}, {kwargs}")

    def __repr__(self):
        try:
            return f"{self.__class__.__name__}(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})"
        except AttributeError:
            return f"{self.__class__.__name__}(custom object)"


class BaseProduct(ABC):
    @abstractmethod
    def get_total_price(self):
        pass

    @abstractmethod
    def reduce_quantity(self, amount):
        pass


class Product(BaseProduct, CreationInfoMixin):
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        CreationInfoMixin.__init__(self, name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сумма всех товаров на складе"""
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        else:
            return self.price * self.quantity + other.price * other.quantity

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

    def get_total_price(self) -> int:
        """Возвращает общую стоимость продукта (цена * количество)."""
        return self.price * self.quantity

    def reduce_quantity(self, amount: int):
        """Уменьшает количество продукта на указанное значение."""
        if amount < 0:
            raise ValueError("Количество не может быть отрицательным")
        if self.quantity < amount:
            raise ValueError("Недостаточно товара на складе")
        self.quantity -= amount

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
            raise TypeError("Можно добавлять только объекты типа Product")

    def add_product(self, product):
        """Счетчик продуктов"""
        Category.__add__(self, product)
        self.product_quantity += product.quantity
        return self.product_quantity

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_quantity} шт."

    def get_products(self):
        return self.__products


class Smartphone(Product):
    efficiency: int
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity}, efficiency={self.efficiency}, model={self.model}, memory={self.memory}, color={self.color})"


class LawnGrass(Product, CreationInfoMixin):
    country: str
    germination_period: int
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity}, country={self.country}, germination_period={self.germination_period}, color={self.color})"

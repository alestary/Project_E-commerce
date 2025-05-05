import pytest

from src.classes import Category, Product, Smartphone, LawnGrass


@pytest.fixture()
def test_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def test_category():
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")


@pytest.fixture()
def test_smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
               "S23 Ultra", 256, "Серый")


@pytest.fixture()
def test_lawn_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


def test_check_product(test_product):
    assert test_product.name == "Samsung Galaxy S23 Ultra"
    assert test_product.description == "256GB, Серый цвет, 200MP камера"
    assert test_product.price == 180000.0
    assert test_product.quantity == 5


def test_check_category(test_category):
    assert test_category.name == "Смартфоны"
    assert (test_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
    assert test_category.get_products() == []


def test_str_product(test_product):
    assert str(test_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_str_category(test_category, test_product):
    test_category.add_product(test_product)
    assert str(test_category) == "Смартфоны, количество продуктов: 5 шт."


def test_product_addition(test_product):
    product2 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    result = test_product + product2
    assert result == 180000.0 * 10


def test_product_add(test_product):
    other_product = Product("Test Product", "Desc", 100.0, 3)
    total_value = test_product + other_product
    assert total_value == 180000.0 * 5 + 100.0 * 3


def test_product_add_invalid_type(test_product):
    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        test_product + "invalid"


def test_category_add_invalid_type(test_category):
    with pytest.raises(TypeError, match="Можно добавлять только объекты типа Product"):
        test_category + "invalid"


def test_smartphone_init(test_smartphone):
    assert test_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert test_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert test_smartphone.price == 180000.0
    assert test_smartphone.quantity == 5
    assert test_smartphone.efficiency == 95.5
    assert test_smartphone.model == "S23 Ultra"
    assert test_smartphone.memory == 256
    assert test_smartphone.color == "Серый"


def test_smartphone_inheritance(test_smartphone):
    assert isinstance(test_smartphone, Product)
    assert str(test_smartphone) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_lawn_grass_init(test_lawn_grass):
    assert test_lawn_grass.name == "Газонная трава"
    assert test_lawn_grass.description == "Элитная трава для газона"
    assert test_lawn_grass.price == 500.0
    assert test_lawn_grass.quantity == 20
    assert test_lawn_grass.country == "Россия"
    assert test_lawn_grass.germination_period == "7 дней"
    assert test_lawn_grass.color == "Зеленый"


def test_lawn_grass_inheritance(test_lawn_grass):
    assert isinstance(test_lawn_grass, Product)
    assert str(test_lawn_grass) == "Газонная трава, 500.0 руб. Остаток: 20 шт."

def test_creation_info_mixin_repr(test_product, test_smartphone, test_lawn_grass):
    """Проверяет строковое представление объектов."""
    assert repr(test_product) == "Product(name=Samsung Galaxy S23 Ultra, description=256GB, Серый цвет, 200MP камера, price=180000.0, quantity=5)"
    assert repr(test_smartphone) == "Smartphone(name=Samsung Galaxy S23 Ultra, description=256GB, Серый цвет, 200MP камера, price=180000.0, quantity=5, efficiency=95.5, model=S23 Ultra, memory=256, color=Серый)"
    assert repr(test_lawn_grass) == "LawnGrass(name=Газонная трава, description=Элитная трава для газона, price=500.0, quantity=20, country=Россия, germination_period=7 дней, color=Зеленый)"

def test_product_get_total_price(test_product):
    """Проверяет метод get_total_price."""
    assert test_product.get_total_price() == 180000 * 5

def test_product_reduce_quantity(test_product):
    """Проверяет метод reduce_quantity."""
    test_product.reduce_quantity(3)
    assert test_product.quantity == 2
    with pytest.raises(ValueError, match="Недостаточно товара на складе"):
        test_product.reduce_quantity(3)
    with pytest.raises(ValueError, match="Количество не может быть отрицательным"):
        test_product.reduce_quantity(-1)
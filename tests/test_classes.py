import pytest

from src.classes import Category, Product


@pytest.fixture()
def test_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def test_category():
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")


def test_check_product(test_product):
    assert test_product.name == "Samsung Galaxy S23 Ultra"
    assert test_product.description == "256GB, Серый цвет, 200MP камера"
    assert test_product.price == 180000.0
    assert test_product.quantity == 5


def test_check_category(test_category):
    assert test_category.name == "Смартфоны"
    assert (test_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
    assert test_category.products == ""


def test_add_product_category(test_category, test_product):
    test_category.add_product_category(test_product)
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт" in test_category.products
    assert Category.product_count == 1

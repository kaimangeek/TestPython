from main import Product, Basket
import pytest

testsSum = [([Product('Tesla', 50), Product('Toyota', 30), Product('Nissan', 20)], 100)]
testsName = [([Product('Tesla', 50)], 'Tesla'), ([Product('Nissan', 20)], 'Nissan')]
testsPrice = [([Product('Tesla', 50)], 50), ([Product('Nissan', 20)], 20)]


@pytest.mark.parametrize('products, s', testsSum)
def test_basket(products, s):
    basket = Basket()
    for x in products:
        basket.add(x)
    assert s == basket.count_sum()


@pytest.mark.parametrize('name, price', testsName)
def test_name(name, price):
    product = Product(name, price)
    assert product.name == name


@pytest.mark.parametrize('name, price', testsPrice)
def test_price(name, price):
    product = Product(name, price)
    assert product.price == price


Tesla = Product('Tesla', 50)
Toyota = Product('Toyota', 30)
Nissan = Product('Nissan', 20)
testsAdd = [([Tesla, Toyota, Nissan],
             [Tesla, Toyota], Nissan)]


@pytest.mark.parametrize('products, products2, products3', testsAdd)
def test_basketAdd(products, products2, products3):
    basket = Basket(products2)
    basket.add(products3)
    assert basket.basket == products


testsRemove = [([Tesla, Toyota, Nissan],
                [Tesla, Toyota], Nissan)]


@pytest.mark.parametrize('products, products2, products3', testsRemove)
def test_basketRemove(products, products2, products3):
    basket = Basket(products)
    basket.remove(products3)
    assert basket.basket == products2

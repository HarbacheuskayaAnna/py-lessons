import pytest

from lesson11_cart import Cart

@pytest.fixture
def cart():
    print("\nSETUP: creating an empty cart")
    yield Cart()
    print("\nTEARDOWN: removing an empty cart")

@pytest.fixture
def filled_cart(cart):
    cart.add("backpack", 30)
    cart.add("t-shirt", 15, qty=2)
    print("\nSETUP: creating a filled cart")
    yield cart
    print("\nTEARDOWN: removing a filled cart")
import pytest


def test_removing_all_items_empty_cart(filled_cart):
    filled_cart.remove("backpack")
    filled_cart.remove("t-shirt")
    assert filled_cart.total() == 0

def test_add_zero_raise_error(filled_cart):
    with pytest.raises(ValueError, match="qty must be positive"):
        filled_cart.add("dress", 50, 0)
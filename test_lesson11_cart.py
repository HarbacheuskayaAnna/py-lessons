import pytest


def test_new_cart_is_empty(cart):
    assert cart.count() == 0

@pytest.mark.smoke
def test_add_one_item(cart):
    cart.add("backpack", 30)
    assert cart.count() == 1


def test_total_for_two_items(filled_cart):
    assert filled_cart.total() == 60

@pytest.mark.smoke
def test_remove_item(filled_cart):
    filled_cart.remove("backpack")
    assert filled_cart.count() == 2

@pytest.mark.smoke
def test_add_same_item_increases_qty(filled_cart):
    filled_cart.add("backpack", 30)
    assert filled_cart.count() == 4


def test_remove_missing_item_raises(filled_cart):
    with pytest.raises(KeyError):
        filled_cart.remove("jacket")
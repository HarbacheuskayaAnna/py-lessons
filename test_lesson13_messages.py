import pytest

def test_filled_cart_total(filled_cart):
    total = filled_cart.total()
    assert total == 60, f"Cart summ: expected 60, but we are getting {total}" 

def test_all_items_have_positive_qty(filled_cart):
    for name, item in filled_cart.items.items():
        assert item["qty"] > 0, f"An item {name} has a quantity - {item['qty']} which is equal or less than 0"
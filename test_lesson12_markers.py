import pytest
import sys

@pytest.mark.skip(reason="feature not ready yet")
def test_apply_coupon(cart):
    cart.apply_coupon("SALE10")

@pytest.mark.skipif(sys.platform == "win32", reason="incorrect platform (win32)")
def test_new_cart_is_empty_on_linux(cart):
    assert cart.count() == 0

@pytest.mark.xfail(reason="Bug-101", strict=True)
def test_negative_price_raises(cart):
    with pytest.raises(ValueError):
        cart.add("bag", -10)

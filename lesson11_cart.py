"""Урок 11. Корзина интернет-магазина (как на saucedemo.com, к ней вернёмся в UI-тестах).

Код уже написан и работает. Сегодня мы не пишем код, а учимся
красиво готовить для тестов данные: фикстуры (fixtures).
"""


class Cart:
    def __init__(self):
        self.items = {}  # имя товара -> {"price": ..., "qty": ...}

    def add(self, name, price, qty=1):
        if qty <= 0:
            raise ValueError("qty must be positive")
        if name in self.items:
            self.items[name]["qty"] += qty
        else:
            self.items[name] = {"price": price, "qty": qty}

    def remove(self, name):
        if name not in self.items:
            raise KeyError(name)
        del self.items[name]

    def count(self):
        """Сколько всего штук товаров в корзине."""
        return sum(item["qty"] for item in self.items.values())

    def total(self):
        """Сумма к оплате."""
        return sum(item["price"] * item["qty"] for item in self.items.values())

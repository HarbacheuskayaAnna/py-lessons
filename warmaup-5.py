# Разминка перед уроком 5: класс + self + dict.get.
# Замени каждый pass на код, потом запусти файл.
# Если все assert прошли, в конце напечатается "Разминка пройдена!".

# Так выглядит "ответ API" (API response): список словарей.
# Обрати внимание: у ключа "id" нет префикса, а "status" есть не у всех.
orders_data = [
    {"id": 101, "total": 250, "status": "paid"},
    {"id": 102, "total": 40},
    {"id": 103, "total": 990, "status": "cancelled"},
]


class Order:
    # 1. Конструктор (__init__): сохрани order_id, total и status в атрибуты.
    #    status по умолчанию (default) "new".
    def __init__(self, order_id, total, status="new"):
        self.order_id = order_id
        self.total = total
        self.status = status

    # 2. True, если заказ оплачен (status == "paid"), иначе False.
    def is_paid(self):
        return self.status == "paid"

    # 3. True, если total больше limit, иначе False.
    def is_big(self, limit):
        if self.total > limit:
            return True
        return False


# 4. Создай список объектов Order из списка словарей.
#    Если "status" в словаре нет, используй "new" (подсказка: dict.get).
def make_orders(data):
    orders = []
    for order in data:
        order = Order(order["id"], order["total"], order.get("status", "new"))
        orders.append(order)
    return orders

# 5. Найди заказ с таким order_id в списке объектов Order.
#    Не нашла — верни None.
def find_order(orders, order_id):
    for order in orders:
        if order.order_id == order_id:
            return order
    return None


# ---------- Проверки (не меняй) ----------
order = Order(1, 100)
assert order.order_id == 1
assert order.total == 100
assert order.status == "new"
assert order.is_paid() is False
assert Order(2, 50, "paid").is_paid() is True

assert order.is_big(50) is True
assert order.is_big(100) is False

orders = make_orders(orders_data)
assert len(orders) == 3
assert orders[0].order_id == 101
assert orders[0].is_paid() is True
assert orders[1].status == "new"
assert orders[2].total == 990

assert find_order(orders, 103).status == "cancelled"
assert find_order(orders, 999) is None

print("Разминка пройдена!")

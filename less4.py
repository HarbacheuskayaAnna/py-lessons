# ============================================================
# Урок 4. Классы (class) и объекты (object)
# ============================================================
#
# Зачем: в автотестах почти всё будет классами.
#   - ApiClient (API-клиент): хранит base_url и token, умеет get/post.
#   - Page Object: страница сайта как класс (LoginPage.login(...)).
#
# Класс (class) = шаблон. Объект (object, instance) = заполненный экземпляр.
# Аналогия: класс = структура таблицы в SQL (колонки),
#           объект = одна строка с конкретными значениями.
#
# Пример (это не задание, просто прочитай и запусти):

class Dog:
    def __init__(self, name, age):   # __init__ вызывается при создании объекта
        self.name = name             # self.name — атрибут (attribute) объекта
        self.age = age

    def greet(self):                 # метод (method) = функция внутри класса
        return f"Woof! I am {self.name}"

    def is_puppy(self):
        return self.age < 1

rex = Dog("Rex", 3)         # создаём объект: Python сам вызывает __init__
print(rex.name)             # Rex   — читаем атрибут через точку
print(rex.greet())          # Woof! I am Rex — вызываем метод
print(rex.is_puppy())       # False

# Главное:
# 1. self = "этот конкретный объект". Первый параметр КАЖДОГО метода.
#    Внутри метода к атрибутам обращаемся через self.: self.name, а не name.
# 2. При вызове self НЕ передаём: rex.greet(), а не rex.greet(rex).
# 3. Методы, как и функции, должны делать return (помним про return!).
# 4. Имя класса пишется с большой буквы: Dog, User, ApiClient (CamelCase).


# ============================================================
# Задание. Напиши код вместо pass, потом запусти файл.
# ============================================================

# 1. Класс User.
#    __init__(self, user_id, email, role="user")  — role по умолчанию "user".
#    Атрибуты: self.user_id, self.email, self.role
#    Методы:
#      is_admin()  -> True, если role == "admin"
#      to_dict()   -> {"id": ..., "email": ..., "role": ...}
#                     (как JSON в ответе API)
class User:
    def __init__(self, user_id, email, role="user"):
        self.user_id = user_id
        self.email = email
        self.role = role

    def is_admin(self):
        if self.role == "admin":
            return True
        return False

    def to_dict(self):
        return {"id":self.user_id, "email":self.email, "role":self.role}

# 2. Функция (не метод!): из списка словарей сделать список объектов User.
#    Если в словаре нет "role", пусть будет роль по умолчанию.
#    Подсказка: у словаря есть метод .get("role", "user").
def make_users(raw_users):
    user_list = []
    for raw_user in raw_users:
        user = User(raw_user["id"], raw_user["email"], raw_user.get("role", "user"))
        user_list.append(user)
    return user_list

# 3. Класс Cart (корзина).
#    __init__(self): self.items = []   (корзина создаётся пустой)
#    Методы:
#      add(product)   -> добавить товар (dict) в self.items, ничего не возвращать
#      count()        -> сколько товаров в корзине
#      total()        -> сумма цен всех товаров
#      is_empty()     -> True, если корзина пустая (вспомни truthiness!)
class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def count(self):
        return len(self.items)

    def total(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total

    def is_empty(self):
        return self.count() == 0

# ---------- Проверки (не меняй) ----------
kate = User(1, "kate@test.com", "admin")
bob = User(2, "bob@test.com")

assert kate.email == "kate@test.com"
assert bob.role == "user"
assert kate.is_admin() is True
assert bob.is_admin() is False
assert bob.to_dict() == {"id": 2, "email": "bob@test.com", "role": "user"}

raw = [
    {"id": 1, "email": "kate@test.com", "role": "admin"},
    {"id": 2, "email": "bob@test.com"},
]
users = make_users(raw)
assert len(users) == 2
assert users[0].is_admin() is True
assert users[1].role == "user"
assert users[1].to_dict() == {"id": 2, "email": "bob@test.com", "role": "user"}

cart = Cart()
assert cart.is_empty() is True
cart.add({"id": 1, "name": "phone", "price": 500})
cart.add({"id": 3, "name": "mouse", "price": 25})
assert cart.count() == 2
assert cart.total() == 525
assert cart.is_empty() is False

other_cart = Cart()
assert other_cart.count() == 0, "У каждой корзины свои items"

print("Урок 4 пройден!")

"""Урок 9. Функции, которые мы будем проверять тестами (tests).

Сейчас функции не дописаны: внутри только `pass` (заглушка, stub).
Задача: дописать их так, чтобы тесты в test_lesson9_users.py стали зелёными.
"""

USERS = [
    {"id": 10, "name": "Anna", "active": True},
    {"id": 20, "name": "Boris", "active": False},
    {"id": 30, "name": "Clara", "active": True},
]


def find_user(users, user_id):
    """Вернуть dict пользователя, у которого поле "id" равно user_id.
    Если такого пользователя нет, вернуть None.
    """
    for user in users:
        if user["id"] == user_id:
            return user
    return None


def active_names(users):
    """Вернуть список имён (name) активных пользователей (active == True),
    в том же порядке, что и в users.
    """
    active_users = []
    for user in users:
        if user["active"]:
            active_users.append(user["name"])
    return active_users


def is_valid_age(age):
    """Возраст валиден, если он от 18 до 65 включительно. Вернуть True или False."""
    return 18 <= age <= 65

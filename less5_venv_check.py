# Урок 5: проверка, что venv и requests работают.
# Запусти этот файл ПОСЛЕ того, как активировала .venv и установила requests.

import sys

import requests

# 1. Какой Python запущен? Если venv активен, в пути будет ".venv".
print("Python:", sys.executable)

# 2. Первый настоящий запрос (request) из кода, как Send в Postman.
response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print("Status code:", response.status_code)

# .json() превращает тело ответа (response body) в обычный dict
user = response.json()
print("Name:", user["name"])
print("Email:", user["email"])

assert response.status_code == 200
assert user["id"] == 1

print("venv и requests работают!")

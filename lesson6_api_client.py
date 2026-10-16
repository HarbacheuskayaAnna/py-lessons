# Урок 6: мини-проект ApiClient (API-клиент, класс-обёртка над requests).
# Замени каждый pass на код, потом запусти файл ИЗ АКТИВИРОВАННОГО .venv.
# Если все assert прошли, в конце напечатается "ApiClient готов!".
#
# Зачем: в автотестах никто не пишет requests.get("https://...") в каждом тесте.
# Базовый адрес, токен и заголовки (headers) живут в одном классе,
# а тест вызывает client.get("/users/1"). Это как Environment в Postman:
# {{base_url}} задан один раз, в запросах только путь.

import requests


class ApiClient:
    # 1. Конструктор: сохрани base_url и token в атрибуты.
    #    token по умолчанию None (без авторизации).
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token

    # 2. Склей base_url и path и верни полный адрес.
    #    ApiClient("https://site.com").build_url("/users/1") -> "https://site.com/users/1"
    def build_url(self, path):
        return self.base_url + path

    # 3. Верни словарь заголовков.
    #    Всегда есть "Content-Type": "application/json".
    #    Если token задан, добавь "Authorization": "Bearer <token>".
    #    Если token None, ключа "Authorization" быть не должно.
    def headers(self):
        headers = {"Content-Type": "application/json"}
        if self.token is None:
            return headers
        headers["Authorization"] = f"Bearer {self.token}"
        return headers

    # 4. Отправь GET на build_url(path) с headers() и верни response (не .json()!).
    def get(self, path):
        endpoint = self.build_url(path)
        response_get = requests.get(endpoint, headers=self.headers())
        return response_get

    # 5. Отправь POST на build_url(path), тело data передай через json=,
    #    заголовки через headers=. Верни response.
    def post(self, path, data):
        response_post = requests.post(self.build_url(path), headers=self.headers(), json=data)
        return response_post

# ---------- Проверки без сети (не меняй) ----------
client = ApiClient("https://jsonplaceholder.typicode.com")
assert client.base_url == "https://jsonplaceholder.typicode.com"
assert client.token is None
assert client.build_url("/users/1") == "https://jsonplaceholder.typicode.com/users/1"
assert client.headers() == {"Content-Type": "application/json"}

auth_client = ApiClient("https://example.com", token="abc123")
assert auth_client.headers()["Authorization"] == "Bearer abc123"
assert auth_client.headers()["Content-Type"] == "application/json"
print("Часть 1 (без сети) пройдена")

# ---------- Проверки с сетью (не меняй) ----------
response = client.get("/users/1")
assert response.status_code == 200
user = response.json()
assert user["id"] == 1
assert user["username"] == "Bret"

response = client.post("/posts", {"title": "autotest", "body": "hi", "userId": 1})
assert response.status_code == 201
created = response.json()
assert created["title"] == "autotest"
assert "id" in created

print("ApiClient готов!")

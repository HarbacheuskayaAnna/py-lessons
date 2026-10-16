# Урок 7, разминка (~15 минут)
# Темы: mutation vs reassignment, self.attr vs параметр, method vs method()
# Заполни места с TODO и запусти файл. Если всё верно, увидишь "Все проверки пройдены!"


# --- Задание 1. Мутирующие методы (mutating methods) возвращают None ---
# Функция добавляет tag в список tags и ВОЗВРАЩАЕТ этот же список.
# Ловушка: list.append() меняет список "на месте" и возвращает None.

def add_tag(tags, tag):
    tags.append(tag)
    return tags


# --- Задание 2. Присваивание по ключу ничего не возвращает ---
# Функция ставит заказу новый статус и возвращает этот же dict.

def set_status(order, status):
    order["status"] = status
    return order


# --- Задание 3. Класс: self.attr vs параметр, method vs method() ---
class Endpoint:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def headers(self):
        # TODO: верни dict {"Authorization": "Bearer <token>"}
        headers_result = {}
        headers_result["Authorization"] = f"Bearer {self.token}"
        return headers_result

    def url(self, path):
        full_url = self.base_url + path
        return full_url

    def describe(self, path):
        # TODO: верни строку "GET <полный url> | headers: <сколько ключей в headers>"
        # Подсказка: используй свои же методы url(...) и headers()
        get_request = f"GET {self.url(path)} | headers: {len(self.headers())}"
        return get_request


# --- Задание 4. Предскажи, БЕЗ запуска ---
# Впиши ответы строками, например "None" или "[1, 2, 3]"
a = [1, 2]
b = a.append(3)
# Что лежит в a? Что лежит в b?
ANSWER_A = "[1, 2, 3]"
ANSWER_B = "None"


# ==================== проверки, не меняй ====================
tags = ["smoke"]
result = add_tag(tags, "api")
assert result == ["smoke", "api"], f"add_tag вернула {result!r}"
assert tags == ["smoke", "api"], "исходный список тоже должен измениться"

order = {"id": 7, "status": "new"}
result = set_status(order, "paid")
assert result == {"id": 7, "status": "paid"}, f"set_status вернула {result!r}"
assert result is order, "должен вернуться тот же самый dict, не копия"

ep = Endpoint("https://api.test", "abc123")
assert ep.headers() == {"Authorization": "Bearer abc123"}, f"headers() вернул {ep.headers()!r}"
assert ep.url("/users") == "https://api.test/users", f"url() вернул {ep.url('/users')!r}"
assert ep.url("/orders") == "https://api.test/orders", "url() должен зависеть от параметра path"
assert ep.describe("/users") == "GET https://api.test/users | headers: 1", f"describe() вернул {ep.describe('/users')!r}"

assert ANSWER_A == str(a), "Задание 4: проверь, что лежит в a"
assert ANSWER_B == str(b), "Задание 4: проверь, что лежит в b"

print("Все проверки пройдены!")

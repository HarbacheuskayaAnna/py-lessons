# Разминка перед уроком 4: повторяем шаблоны из урока 3.
# Напиши функции с нуля (вместо pass), потом запусти файл.
# Если все assert прошли, в конце напечатается "Разминка пройдена!".

products = [
    {"id": 1, "name": "phone", "price": 500},
    {"id": 2, "name": "laptop", "price": 1200},
    {"id": 3, "name": "mouse", "price": 25},
]

# 1. Поиск в цикле (search in loop).
# Верни товар (весь dict) с таким name. Если не нашла, верни None.
def find_product_by_name(products, name):
    for product in products:
        if product["name"] == name:
            return product
    return None

# 2. То же самое, но если не нашла, выбрось (raise) ValueError
#    с сообщением f"Product {product_id} not found".
def get_product_by_id(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    raise ValueError(f"Product {product_id} not found")

# 3. Маленькая функция-помощник (helper): True, если код успешный (200..299).
def is_success(status_code):
    if 200 <= status_code <= 299:
        return True
    return False

# 4. Вызов функции для каждого элемента списка.
# Верни список кодов, которые НЕ успешные. Используй is_success внутри.
def get_failed_codes(codes):
    list_of_codes = []
    for code in codes:
        if not is_success(code):
            list_of_codes.append(code)
    return list_of_codes

# 5. Truthiness: верни "OK", если ошибок нет, иначе "FAILED: [500, 404]".
# Используй get_failed_codes и проверку `if failed:` (без len и без == []).
def build_report(codes):
    failed = get_failed_codes(codes)
    if failed:
        return f"FAILED: {failed}"
    return "OK"


# ---------- Проверки (не меняй) ----------
assert find_product_by_name(products, "mouse") == {"id": 3, "name": "mouse", "price": 25}
assert find_product_by_name(products, "phone")["price"] == 500
assert find_product_by_name(products, "tablet") is None

assert get_product_by_id(products, 2)["name"] == "laptop"
try:
    get_product_by_id(products, 99)
    assert False, "Должна была быть ValueError"
except ValueError as error:
    assert str(error) == "Product 99 not found"

assert is_success(200) is True
assert is_success(299) is True
assert is_success(300) is False
assert is_success(199) is False

assert get_failed_codes([200, 500, 201, 404]) == [500, 404]
assert get_failed_codes([200, 204]) == []

assert build_report([200, 201]) == "OK"
assert build_report([200, 500, 404]) == "FAILED: [500, 404]"

print("Разминка пройдена!")

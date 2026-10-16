users = [
    {"id": 1, "email": "anna@test.com", "role": "admin", "active": True},
    {"id": 2, "email": "bob@test.com", "role": "user", "active": False},
    {"id": 3, "email": "kate@test.com", "role": "user", "active": True},
]

email = "Kate@Test.com "
email.strip().lower()        # "kate@test.com": убрать пробелы, в нижний регистр
"@" in email                 # True: подстрока есть
"kate@test.com".split("@")   # ["kate", "test.com"]: строка -> список
f"User {email} not found"    # f-string: подставляет значения в {}

response = {"id": 3, "email": "kate@test.com"}
for key, value in response.items():   # обход ключей и значений
    print(f"{key} = {value}")
"id" in response             # True: проверка наличия КЛЮЧА

ids = [u["id"] for u in users]  # list comprehension: [1, 2, 3]


def get_emails(users):
    mail_list = [u["email"] for u in users]
    return mail_list

def format_user(user):
    return f'#{user["id"]} {user["email"]} ({user["role"]})'

def is_valid_email(email):
    result = False
    if email.count('@') == 1:
        list_email = email.split("@")
        second_part = list_email[1]
        if email.count('@') == 1 and email == email.strip() and '.' in second_part :
            result = True
    return result

def find_missing_fields(response, required):
    notin_list = []
    for i in required:
        if i not in response:
            notin_list.append(i)
    return notin_list

assert get_emails(users) == ["anna@test.com", "bob@test.com", "kate@test.com"]
assert format_user(users[2]) == "#3 kate@test.com (user)"
assert is_valid_email("kate@test.com") is True
assert is_valid_email("katetest.com") is False
assert is_valid_email("kate@@test.com") is False
assert is_valid_email("kate@testcom") is False
assert find_missing_fields({"id": 1, "email": "a@test.com"}, ["id", "email", "role"]) == ["role"]
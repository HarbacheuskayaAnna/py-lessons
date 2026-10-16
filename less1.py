users = [
    {"id": 1, "email": "anna@test.com", "role": "admin", "active": True},
    {"id": 2, "email": "bob@test.com", "role": "user", "active": False},
    {"id": 3, "email": "kate@test.com", "role": "user", "active": True},
]

def is_success(code):          # параметр (parameter)
    return 200 <= code < 300   # return отдаёт результат наружу

codes = [200, 404, 500]        # list: упорядоченный набор, codes[0] == 200
user = {"email": "a@test.com", "active": True}  # dict: ключ -> значение, user["email"]

for c in codes:
    print(c, is_success(c))

def get_status_group(code):
    if 200 <= code <= 299:
        return 'success'
    elif 400 <= code <= 499:
        return 'client error'
    elif 500 <= code <= 599:
        return 'server error'
    else:
        return 'unknown'



def get_active_users(users):
    result_users = []
    for user in users:
        if user["active"]:
            result_users.append(user)
    return result_users


def find_user_by_email(users, email):
    for user in users:
        if user['email'] == email:
            return user
    return None


assert get_status_group(404) == 'client error'
assert get_status_group(505) == 'server error'
assert get_status_group(199) == 'unknown'
found_user = find_user_by_email(users, "kate@test.com")
assert found_user["id"] == 3
assert found_user["email"] == "kate@test.com"
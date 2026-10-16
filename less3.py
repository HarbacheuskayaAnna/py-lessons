import json

def load_users(file_path):
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
        return data

def get_user_by_id(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    raise ValueError(f"User with id {user_id} not found")
    

def parse_status_code(code):
    try:
        code = int(code)
    except ValueError:
        code = None
    return code

def find_missing_fields(response, required):
    notin_list = []
    for i in required:
        if i not in response:
            notin_list.append(i)
    return notin_list

def find_invalid_users(users, required):
    invalid_ids = []
    for user in users:
        missing = find_missing_fields(user, required)
        if missing:
            invalid_ids.append(user["id"])
    return invalid_ids

users = load_users("users.json")
assert len(users) == 4
assert get_user_by_id(users, 3)["email"] == "kate@test.com"
assert parse_status_code("404") == 404
assert parse_status_code("abc") is None
assert find_invalid_users(users, ["id", "email", "role"]) == [4]
from lesson9_users import USERS, find_user, active_names, is_valid_age

import pytest

# ---------- find_user ----------

def test_find_user_returns_user_by_id():
    user = find_user(USERS, 20)
    assert user["name"] == "Boris"


def test_find_user_finds_last_user():
    user = find_user(USERS, 30)
    assert user is not None
    assert user["name"] == "Clara"


def test_find_user_returns_none_for_unknown_id():
    assert find_user(USERS, 99) is None


# ---------- active_names ----------

def test_active_names_returns_only_active():
    assert active_names(USERS) == ["Anna", "Clara"]


def test_active_names_empty_list():
    assert active_names([]) == []


# ---------- is_valid_age ----------
# Задание 3: напиши тесты для is_valid_age сама.
# Подумай как тестировщик: какие значения проверить на границах (boundary values)?

@pytest.mark.parametrize("age, expected", [
    (18, True, ),
    (65, True),
    (64, True),
    (19, True),
    (17, False),
    (66, False),
    (-60, False)
], ids =["min-valid age", "max-valid age", "max-1-valid age", "min+1-valid age", "min-1-invalid age", "max+1-invalid age", "negative - no such age"])
def test_is_valid_age(age, expected):
    assert is_valid_age(age) is expected
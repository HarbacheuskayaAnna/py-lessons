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

@pytest.mark.parametrize("age, expected", [
    pytest.param(18, True, id="min"),
    pytest.param(65, True, id="max"),
    pytest.param(64, True, id="max-1"),
    pytest.param(19, True, id="min+1"),
    pytest.param(17, False, id="min-1"),
    pytest.param(66, False, id="max+1"),
    pytest.param(-60, False, id="neg_value"),
])
def test_is_valid_age(age, expected):
    assert is_valid_age(age) is expected
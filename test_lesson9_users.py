from lesson9_users import USERS, find_user, active_names, is_valid_age


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
def test_is_valid_age_pos_18():
    assert is_valid_age(18) is True

def test_is_valid_age_pos_65():
    assert is_valid_age(65) is True

def test_is_valid_age_pos_64():
    assert is_valid_age(64) is True

def test_is_valid_age_pos_19():
    assert is_valid_age(19) is True

def test_is_valid_age_neg_17():
    assert is_valid_age(17) is False

def test_is_valid_age_neg_66():
    assert is_valid_age(66) is False

def test_is_valid_age_negative():
    assert is_valid_age(-60) is False
import pytest

from lesson10_validators import parse_age


# Задание 4: тесты для parse_age.
# 1) один параметризованный тест для валидных строк: (text, expected)
# 2) один параметризованный тест для невалидных строк через pytest.raises

@pytest.mark.parametrize("text, expected", [
    ("0", 0),
    ("120", 120),
    ("1", 1),
    (" 25 ", 25)
], ids =["min-valid age", "max-valid age", "min+1-valid age", "cut_spaces"])
def test_parse_age(text, expected):
    assert parse_age(text) == expected


@pytest.mark.parametrize("text", [
    ("abs"),
    ("-1"),
    ("121"),
    ("120.99"),
    ("")])
def test_parse_age_invalid(text):
    with pytest.raises(ValueError):
        parse_age(text)
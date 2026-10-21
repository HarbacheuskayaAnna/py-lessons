import pytest

from lesson10_validators import parse_age

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
    ("")], ids =["string-invalid age", "min-invalid age", "max-invalid age", "float-invalid", "empty string"])
def test_parse_age_invalid(text):
    with pytest.raises(ValueError):
        parse_age(text)
import pytest

from lesson10_validators import parse_age

@pytest.mark.parametrize("text, expected", [
    ("1", 1),
    ("119", 119),
    ("2", 2),
    (" 25 ", 25)
], ids =["min-valid age", "max-valid age", "min+1-valid age", "cut_spaces"])
def test_parse_age(text, expected):
    assert parse_age(text) == expected


@pytest.mark.parametrize("text", [
    ("abs"),
    ("-1"),
    ("0"),
    ("120"),
    ("119.99"),
    ("")], ids =["string-invalid age", "negative-invalid age", "0 - invalid age", "max+1-invalid age", "float-invalid", "empty string"])
def test_parse_age_invalid(text):
    with pytest.raises(ValueError):
        parse_age(text)
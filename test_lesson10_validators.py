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
    (""),
    ("25.99")], ids =["string", "float", "empty"])
def test_parse_age_not_integer(text):
    with pytest.raises(ValueError):
        parse_age(text)

@pytest.mark.parametrize("text", [
    ("-1"),
    ("121")], ids =["min-1", "max+1"])
def test_parse_age_out_of_range(text):
    with pytest.raises(ValueError, match="out of range"):
        parse_age(text)
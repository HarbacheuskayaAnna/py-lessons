import pytest

from lesson10_validators import parse_age

@pytest.mark.parametrize("text, expected", [
    pytest.param("0", 0, id="min"),
    pytest.param("120", 120, id="max"),
    pytest.param("1", 1, id="min+1"),
    pytest.param(" 25 ", 25, id="cut spaces")
])
def test_parse_age(text, expected):
    assert parse_age(text) == expected


@pytest.mark.parametrize("text", [
    pytest.param("abs", id="string"), 
    pytest.param("", id="empty string"),
    pytest.param("25.99", id="float")])
def test_parse_age_not_integer(text):
    with pytest.raises(ValueError):
        parse_age(text)

@pytest.mark.parametrize("text", [
    pytest.param("-1", id="min-1"),
    pytest.param("121", id="max+1")])
def test_parse_age_out_of_range(text):
    with pytest.raises(ValueError, match="out of range"):
        parse_age(text)
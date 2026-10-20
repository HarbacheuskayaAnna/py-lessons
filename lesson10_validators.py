"""Урок 10. Функция для задания на pytest.raises.

Сейчас внутри только `pass` (заглушка, stub). Допиши её сама.
"""


def parse_age(text):
    """Превратить возраст из поля формы (строка) в int.

    Требования:
    - "25" -> 25
    - " 25 " -> 25 (пробелы по краям не мешают)
    - если в строке не целое число ("abc", "", "25.5") -> ValueError
    - если число меньше 0 или больше 120 -> ValueError("age out of range")
    """
    if int(text) < 0:
        raise ValueError(f"age out of range")
    if int(text) > 120:
        raise ValueError(f"age out of range")
    return int(text)

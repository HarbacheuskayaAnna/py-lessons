def parse_age(text):
    """Превратить возраст из поля формы (строка) в int.
 
    Требования:
    - "25" -> 25
    - " 25 " -> 25 (пробелы по краям не мешают)
    - если в строке не целое число ("abc", "", "25.5") -> ValueError
    - если число меньше 0 или больше 120 -> ValueError("age out of range")
    """
    age = int(text)
    if not 0 <= age <= 120:
        raise ValueError("age out of range")
    return age

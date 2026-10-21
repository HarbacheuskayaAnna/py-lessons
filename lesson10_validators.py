def parse_age(text):
    age = int(text)
    if not 0 < age < 120:
        raise ValueError(f"age out of range")
    return age

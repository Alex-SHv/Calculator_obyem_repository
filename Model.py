# model.py
conversion = {
    "м3": 1,
    "дм3": 0.001,
    "см3": 0.000001,
    "мм3": 0.000000001
}

def convert(value, from_unit, to_unit):
    try:
        value = float(value)
    except ValueError:
        return None, "Ошибка: введите число!"

    if from_unit not in conversion or to_unit not in conversion:
        return None, "Ошибка: используйте только м3, дм3, см3 или мм3!"

    value_in_m3 = value * conversion[from_unit]
    result = value_in_m3 / conversion[to_unit]
    return result, None
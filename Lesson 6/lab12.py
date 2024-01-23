def count(num):
    num = abs(num)
    a = str(num)
    return len(a)


print(f"Количество цифр равно: {count(-12334)}")


def count1(num):
    import re
    a = str(num)
    digits = re.findall(r'\d', a)
    return len(digits)


print(f"Количество цифр равно: {count1("-12a33a34")}")

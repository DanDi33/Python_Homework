def multiply(num1, num2):
    res = 1
    if num1 > num2:
        num1, num2 = num2, num1
    for i in range(num1, num2 + 1):
        res *= i
    return res


print(f"Произведение чисел диапазона равно: {multiply(5, 1)}")

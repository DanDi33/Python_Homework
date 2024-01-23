a = int(input("Введите 1ое число: "))
b = int(input("Введите 2ое число: "))
c = int(input("Введите 3ое число: "))
check = int(input("Что считаем?"
                  "\n\t1. Minimum"
                  "\n\t2. Maximum"
                  "\n\t3. Average"
                  "\n\tВведите число: "))
print("*" * 30)
if check == 1:
    print(f"Минимум чисел {a}, {b}, {c} это: {min(a, b, c)}")
elif check == 2:
    print(f"Максимум чисел {a}, {b}, {c} это: {max(a, b, c)}")
elif check == 3:
    print(f"Среднее значение чисел {a}, {b}, {c} равно: {round((a + b + c) / 3, 2)}")
else:
    print("Вы ввели некорректное значение")

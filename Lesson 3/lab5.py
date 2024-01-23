x = int(input("Введите число: "))
y = int(input(f"Введите степень в которую возвести '{x}': "))
if x != 0:
    res = 1
else:
    res = 0
if y >= 0:
    # res = x**y
    for elem in range(y):
        res = res * x
    print("*" * 30)
    print(f"Результат: {res}")
else:
    print("Некорректное значение степени. Степень должна быть больше или равна нулю.")

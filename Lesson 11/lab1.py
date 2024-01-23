import random

try:
    a = int(input("Введите длину массива: "))
except:
    print("Некорректное значение. Длина массива установлена по умолчанию равной 15")
    a = 15
arr = []
[arr.append(random.randint(-a, a)) for i in range(a)]
print(f"Рандомный массив(список) длиной { len(arr)}: {arr}")
print(f"Среднее арифметическое: {sum(arr) / len(arr)}")
if sum(arr) / len(arr) > 0:
    end_range = len(arr) // 3 * 2
    print("1ые 2/3 массива(списка) сортируем, остальное реверсируем")
else:
    end_range = len(arr) // 3
    print("1ую 1/3 массива(списка) сортируем, остальное реверсируем")
temp = arr[end_range:]
arr = arr[:end_range] + temp[::-1]
i = 1
while i < end_range:
    if arr[i - 1] > arr[i]:
        arr[i - 1], arr[i] = arr[i], arr[i - 1]
        i = 0
    i += 1

print(f"Итоговый массив(список): {arr}")

import random

arr1 = list()
arr2 = list()
arr3 = []
for j in range(1, 11):
    arr1.append(random.randint(-10, 10))
    arr2.append(random.randint(-10, 10))
print("Массив 1")
print(arr1)
print("Массив 2")
print(arr2)

# Объединяю 2 массива
arr3.extend(arr1)
arr3.extend(arr2)
print("Массив, содержащий элементы обоих списков")
print(arr3)

# В каждом из двух массивов удаляю повторяющиеся значения
# Затем объединяю массивы 1 и 2 в массив 3
arr3.clear()
arr1_1 = arr1.copy()
arr2_1 = arr2.copy()
for el in arr1_1:
    if el not in arr3:
        arr3.append(el)
temp = []
for el in arr2_1:
    if el not in temp:
        temp.append(el)
arr3.extend(temp)
print("Массивы очищены от повторений, затем объединены")
print(arr3)

# ищу элементы общие для двух списков
arr3.clear()
for elem in arr1:
    if elem in arr2:
        arr3.append(elem)
print("Массив, содержащий элементы общие для двух списков")
print(arr3)

# Сначала объединяю массивы потом, убираю из массива повторяющиеся значения.
arr3.clear()
temp = []
temp.extend(arr1)
temp.extend(arr2)
for el in temp:
    if el not in arr3:
        arr3.append(el)
print("Массив, содержащий только уникальные элементы каждого из списков")
print(arr3)

# Массив содержит только минимальное и максимальное значение каждого из 2 массивов
arr3.clear()
minValue = arr1[0]
maxValue = arr1[0]
for el in arr1:
    if minValue > el:
        minValue = el
    if maxValue < el:
        maxValue = el
arr3.append(minValue)
arr3.append(maxValue)
minValue = arr2[0]
maxValue = arr2[0]
for elem in arr2:
    if minValue > elem:
        minValue = elem
    if maxValue < elem:
        maxValue = elem
arr3.append(minValue)
arr3.append(maxValue)
print("Массив содержит только минимальное и максимальное значение каждого из 2 массивов")
print(arr3)

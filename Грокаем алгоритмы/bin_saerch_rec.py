import random

arr1 = list()
for j in range(1, 101):
    arr1.append(random.randint(0, 1000))
i = 1
while i < (len(arr1)):
    if arr1[i - 1] > arr1[i]:
        arr1[i - 1], arr1[i] = arr1[i], arr1[i - 1]
        i = 0
    i += 1
print(arr1)

lookingFor = int(input("Введите число для поиска: "))


def bin_search(arr, find, low_index=None, middle_index=None, high_index=None):
    if low_index is None:
        low_index = 0
    if high_index is None:
        high_index = len(arr) - 1
    if middle_index is None:
        middle_index = int((low_index + high_index) / 2)
    if find == arr[middle_index]:
        return print(f"Искомое число в массиве найдено под индексом: {middle_index}")
    if middle_index == low_index or middle_index == high_index:
        return print(f"Числа {find} нет в массиве")
    if find < arr[middle_index]:
        return bin_search(arr, find, low_index=low_index, middle_index=int((low_index + middle_index) / 2),
                          high_index=middle_index)
    elif find > arr[middle_index]:
        return bin_search(arr, find, low_index=middle_index, middle_index=int((middle_index + high_index + 1) / 2),
                          high_index=high_index)


bin_search(arr1, lookingFor)

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
lowIndex = 0
highIndex = len(arr1) - 1
middleIndex = int((lowIndex + highIndex) / 2)
count = 0
while lowIndex <= highIndex:
    count += 1
    if lookingFor == arr1[middleIndex]:
        print(f"Искомое число в массиве найдено под индексом: {middleIndex}")
        break
    if middleIndex == lowIndex or middleIndex == highIndex:
        print(f"Числа {lookingFor} нет в массиве")
        break
    if lookingFor < arr1[middleIndex]:
        highIndex = middleIndex
        middleIndex = int((lowIndex + highIndex) / 2)
        # print(f"low: {lowIndex}")
        # print(f"mid: {middleIndex}")
        # print(f"high: {highIndex}")
    else:
        lowIndex = middleIndex
        middleIndex = int((lowIndex+highIndex+1) / 2)
        # print(f"low: {lowIndex}")
        # print(f"mid: {middleIndex}")
        # print(f"high: {highIndex}")
print(f"Количество итераций равно: {count}")

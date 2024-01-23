import random

arr1 = list()
for j in range(1, 11):
    arr1.append(random.randint(0, 100))
print(arr1)
i = 1
while i < (len(arr1)):
    if arr1[i - 1] > arr1[i]:
        arr1[i - 1], arr1[i] = arr1[i], arr1[i - 1]
        i = 0
    i += 1
print(arr1)

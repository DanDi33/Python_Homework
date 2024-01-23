import random

arr1 = list()
for j in range(1, 11):
    arr1.append(random.randint(0, 100))


print(arr1)


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = int(len(arr) / 2)
    pivot_value = [arr.pop(pivot)]
    left_side = []
    right_side = []
    while len(arr) != 0:
        if pivot_value[0] > arr[0]:
            left_side.append(arr.pop(0))
        else:
            right_side.append(arr.pop(0))
    return quick_sort(left_side)+pivot_value+quick_sort(right_side)


print(quick_sort(arr1))

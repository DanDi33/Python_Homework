arr1 = [1, 2, 3, 14, 5]
print(arr1)


def sum_rec(arr, index=None):
    if not arr:
        return 0
    if index is None:
        index = len(arr) - 1
    if index == 0:
        return arr[0]
    else:
        return arr[index] + sum_rec(arr, index=index - 1)


print(f"Сумма массива равна: {sum_rec(arr1)}")

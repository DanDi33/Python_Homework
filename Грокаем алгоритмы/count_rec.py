arr1 = [1, 2, 3, 4, 5]
print(arr1)


def count_rec(arr, index=None):
    if not arr:
        return 0
    if index is None:
        index = len(arr) - 1
    if index == 0:
        return 1
    else:
        return 1 + count_rec(arr, index=index-1)


print(f"Количество элементов в массиве: {count_rec(arr1)}")

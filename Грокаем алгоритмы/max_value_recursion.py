arr1 = [1, 2, 3, 14, 5]
print(arr1)


def max_value_rec(arr, index=None, biggest=None):
    if not arr:
        return 0
    if index is None:
        index = len(arr) - 1
    if biggest is None:
        biggest = arr[index]
    if biggest < arr[index]:
        biggest = arr[index]
    if index == 0:
        return arr1[0] if arr1[0] > biggest else biggest
    else:
        return biggest if biggest > max_value_rec(arr, index=index - 1, biggest=biggest) \
            else max_value_rec(arr, index=index - 1, biggest=biggest)


print(f"Максимальное значение массива: {max_value_rec(arr1)}")
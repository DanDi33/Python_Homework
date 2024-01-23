arr1 = [1, 2, 3, 14, 5]
print(arr1)


def sum_rec(arr):
    temp = arr.copy()
    if not temp:
        return 0
    if len(temp) == 1:
        return arr[0]
    else:
        last = temp.pop()
        return last + sum_rec(temp)


print(sum_rec(arr1))

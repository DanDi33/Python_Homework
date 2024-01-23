def del_int(num, arr):
    res = arr.count(num)
    for i in range(arr.count(num)):
        arr.remove(num)
    # print(arr)
    return res


print(del_int(1, [1, 3, 2, 4, 5, 6, 1, 5, 6, 8, 1]))

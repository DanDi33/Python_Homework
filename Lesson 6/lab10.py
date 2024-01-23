def min_nums(a, b, c, d, e):
    return min(a, b, c, d, e)


print(min_nums(2, -3, 6, 1, 0))


def min_num(a, b, c, d, e):
    arr = [b, c, d, e]
    for el in arr:
        if el < a:
            a = el
    return a


print(min_num(2, 3, 6, 1, 0))

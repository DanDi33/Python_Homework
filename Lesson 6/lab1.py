def product_of_numbers(*numbers):
    res = 1
    for el in numbers:
        res *= el
    return res


print((product_of_numbers(1, 2, 3, 4, 5)))

def min_of_numbers(*numbers):
    # Вариант 1
    # return min(numbers)

    # Вариант 2
    minim = numbers[0]
    for el in numbers:
        if el < minim:
            minim = el
    return minim


print(min_of_numbers(10, 2, 0, 4, 3))

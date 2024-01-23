def exponentiation(exp, /, arr):
    temp = []
    for elem in arr:
        temp.append(elem ** exp)
    return temp


print(exponentiation(2, [1, 2, 3, 4, 5]))

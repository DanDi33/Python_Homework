def even_num(num1, num2):
    if num1 > num2:
        a = -1
        num2 -= 1
    else:
        a = 1
        num2 += 1
    for i in range(num1, num2, a):
        if i % 2 == 0 and i != 0:
            print(i, end=", ")


even_num(10, -10)

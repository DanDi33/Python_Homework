maxNum = 0
minNum = 0
sumNum = 0
while True:
    num = int(input("Введите число: "))
    if num == 7:
        print("Good bye!")
        break
    sumNum += num
    print(f"Сумма чисел равна: {sumNum}")
    if num > maxNum:
        maxNum = num
    elif num < minNum:
        minNum = num
    print(f"Максимум введенных чисел: {maxNum}")
    print(f"Минимум введенных чисел: {minNum}")
    print("*"*30)

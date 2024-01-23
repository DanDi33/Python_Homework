startNum = int(input("Введите число (начало диапазона): "))
endNum = int(input("Введите число (конец диапазона): "))
evenNum = 0
oddNum = 0
nineNum = 0
averageEven = 0
averageNine = 0
averageOdd = 0
if startNum > endNum:
    tmp = endNum
    endNum = startNum
    startNum = tmp
if startNum != endNum:
    while startNum <= endNum:
        if startNum != 0:
            if startNum % 2 == 0:
                averageEven += 1
                evenNum += startNum
            else:
                averageOdd += 1
                oddNum += startNum
            if startNum % 9 == 0:
                averageNine += 1
                nineNum += startNum
        startNum += 1
    print("*" * 30)
    print(f"Сумма четных чисел диапазона равна: {evenNum}, среднеарифметическое равно: {evenNum / averageEven}")
    print(f"Сумма нечетных чисел диапазона равна: {oddNum}, среднеарифметическое равно: {oddNum / averageOdd}")
    print(f"Сумма кратных 9 чисел диапазона равна: {nineNum}, среднеарифметическое равно: {nineNum / averageNine}")
else:
    print("Числа диапазона равны")
while True:
    num = int(input("Введите число: "))
    if num == 7:
        print("Good bye!")
        break
    if num > 0:
        print("Number is positive")
    elif num == 0:
        print("Number is equal to zero")
    else:
        print("Number is negative")

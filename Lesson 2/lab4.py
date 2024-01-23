a = int(input("Введите число в диапазоне от 1 до 100: "))
if 1 <= a <= 100:
    if a % 3 == 0:
        if a % 5 == 0:
            print("Fizz Buzz")
        else:
            print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    else:
        print(a)
else:
    print("Некорректное значение")

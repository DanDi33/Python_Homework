a = int(input("Введите число: "))
check = int(input("В какую степень от 0 до 7 возвести Ваше число?"
                  "\n\tВведите число: "))
print("*"*30)
if 0 <= check <= 7:
    print(f"Ваше число {a} в степени {check} равно: {a**check}")
else:
    print("Некорректное значение степени")

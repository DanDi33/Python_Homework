a = int(input("Введите количество метров: "))
check = int(input("Что считаем?"
                  "\n\t1. Мили"
                  "\n\t2. Дюймы"
                  "\n\t3. Ярды"
                  "\n\tВведите число: "))
print("*" * 30)
if check == 1:
    print(f"В милях это: {round(a / 1609.34, 5)}")
elif check == 2:
    print(f"В дюймах это: {round(a / 0.025, 2)}")
elif check == 3:
    print(f"В ярдах это: {round(a / 0.9144, 2)}")
else:
    print("Вы ввели некорректное значение")

str_pol = input("Введите строку: ")
str_pol = str_pol.replace(" ", "")
str_pol = str_pol.replace(".", "")
str_pol = str_pol.replace(",", "")
str_pol = str_pol.lower()
str_pol = list(str_pol)
middle_index = int(len(str_pol) / 2)  # ищу индекс среднего элемента массива(для нечетной длины - точное указание,
                                        # для нечетной - следующий индекс от середины)
for i in range(middle_index):
    if len(str_pol) % 2 != 0:  # проверяю четное или нечетное количество букв в строке, если нечетное, то ...
        if str_pol[middle_index - (i + 1)] != str_pol[middle_index + (i + 1)]:
            print("Это не палиндром")
            break
    else:  # если четное, то ...
        if str_pol[middle_index - (i + 1)] != str_pol[middle_index + i]:
            print("Это не палиндром")
            break
else:
    print("Это палиндром")

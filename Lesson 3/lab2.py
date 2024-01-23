randomSym = input("Введите любой символ: ")
quantity = int(input(f"Сколько раз повторить '{randomSym}'? "))
if quantity > 0:
    print("*"*30)
    for i in range(quantity):
        print(randomSym)
else:
    print("Количество повторений должно быть больше нуля.")

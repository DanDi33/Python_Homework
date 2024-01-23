side = int(input("Введите сторону квадрата: "))
while True:
    choice = input("\nВыберете фигуру: \n\n"
                   "1. Треугольник прижат к правому верхнему углу;\n"
                   "2. Треугольник прижат к левому нижнему углу;\n"
                   "3. Треугольник прижат к верхней стороне;\n"
                   "4. Треугольник прижат к нижней стороне;\n"
                   "5. Два треугольника прижаты к верхней и нижней сторонам;\n"
                   "6. Два треугольника прижаты к левой и правой сторонам;\n"
                   "7. Треугольник прижат к левой стороне;\n"
                   "8. Треугольник прижат к правой стороне;\n"
                   "9. Треугольник прижат к левому верхнему углу;\n"
                   "0. Треугольник прижат к правому нижнему углу;\n\n"
                   "Введите число от 0 до 9: ")
    print()
    if choice == "1":
        for i in range(side):
            for j in range(side):
                if j >= i or i == (side - 1) or j == 0:
                    print("*", end="  ")
                else:
                    print("   ", end="")
            print()

    elif choice == "2":
        for i in range(side):
            for j in range(side):
                # print(f"j = {j}\n (y-1) = {y-1}")
                if j <= i or j == (side - 1) or i == 0:
                    print("*", end="  ")
                else:
                    print("   ", end="")
            print()

    elif choice == "3":
        for i in range(side):
            for j in range(side):
                if i <= j and i < side - j or j == 0 or j == side - 1 or i == side - 1:
                    print("*", end="  ")
                else:
                    print("   ", end="")
            print()

    elif choice == "4":
        for i in range(side):
            for j in range(side):
                if i + 1 > j and i + 1 >= side - j or i == 0 or j == 0 or j == side - 1:
                    print("*", end="  ")
                else:
                    print("   ", end="")
            print()

    elif choice == "5":
        for i in range(side):
            for j in range(side):
                if (i + 1 > j and i + 1 >= side - j) or (i <= j and i < side - j) or j == 0 or j == side - 1:
                    print("*", end="  ")
                else:
                    print("   ", end="")
            print()

    elif choice == "6":
        for i in range(side):
            for j in range(side):
                if (j + 1 > i and j + 1 >= side - i) or (j <= i and j < side - i) or i == 0 or i == side - 1:
                    print("*", end="  ")
                else:
                    print("   ", end="")
            print()

    elif choice == "7":
        for i in range(side):
            for j in range(side):
                if j <= i and j < side - i or i == 0 or i == side - 1 or j == (side - 1):
                    print("*", end="  ")
                else:
                    print("   ", end="")
            print()

    elif choice == "8":
        for i in range(side):
            for j in range(side):
                if j + 1 > i and j + 1 >= side - i or j == 0 or i == side - 1 or i == 0:
                    print("*", end="  ")
                else:
                    print("   ", end="")
            print()

    elif choice == "9":
        for i in range(side, 0, -1):
            for j in range(side):
                if j < i or j == side - 1 or i == 1:
                    print("*", end="  ")
                else:
                    print("   ", end="")
            print()

    elif choice == "0":
        for i in range(side, 0, -1):
            for j in range(side):
                if j + 1 >= i or j == 0 or i == side:
                    print("*", end="  ")
                else:
                    print("   ", end="")
            print()
    else:
        print("Вы ввели некорректное значение.")
    escape = input('\nВы хотите выйти("y"/"n")? ')
    if escape == "y":
        break

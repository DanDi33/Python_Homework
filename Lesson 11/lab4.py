def menu_list():
    print("\n\t\t\"Справочник\"\n")
    print("1. Отсортировать по идентификационным кодам\n"
          "2. Отсортировать по номерам телефона\n"
          "3. Вывести список пользователей с кодами и телефонами\n"
          "4. Выход.")
    match input("\nВведите число: "):
        case "1":
            bubble_sort(codes, phone_numbers)
            print('справочник отсортирован по идентификационным кодам')
            if input("\n\tПерейти в главное меню(y/n)? ") == "y":
                menu_list()
        case "2":
            bubble_sort(phone_numbers, codes)
            print('справочник отсортирован по номерам телефона')
            if input("\nПерейти в главное меню(y/n)? ") == "y":
                menu_list()
        case "3":
            show_list()
            if input("\nПерейти в главное меню(y/n)? ") == "y":
                menu_list()
        case "4":
            if input("\nВы точно хотите выйти(y/n)? ") == "y":
                print("\nХорошего дня. До свидания")
            else:
                menu_list()
        case _:
            print("\nНекорректный ввод")
            if input("\nПерейти в главное меню(y/n)? ") == "y":
                menu_list()


def show_list():
    for i, elem in enumerate(codes):
        print(f'id: {elem},  номер: {phone_numbers[i]}')


def bubble_sort(first, second):
    n = len(first)
    check = True
    for i in range(n - 1):
        for j in range(n - i - 1):
            if first[j] > first[j + 1]:
                first[j], first[j + 1] = first[j + 1], first[j]
                second[j], second[j + 1] = second[j + 1], second[j]
                check = False
        if check:
            break


codes = [23451, 94842, 21452, 77694, 10002]
phone_numbers = ["+79996775555", "+79005671111", "+79029992222", "+79107773333", "+79205754444"]
menu_list()

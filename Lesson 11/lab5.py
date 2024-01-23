def menu_list():
    print("\n\t\t\"Книги\"\n")
    print("1. Отсортировать по названию книг;\n"
          "2. Отсортировать по годам выпуска;\n"
          "3. Вывести список книг\n"
          "4. Выход.")
    match input("\nВведите число: "):
        case "1":
            bubble_sort(names, years)
            print('справочник отсортирован по названию книг')
            if input("\n\tПерейти в главное меню(y/n)? ") == "y":
                menu_list()
        case "2":
            bubble_sort(years, names)
            print('справочник отсортирован по годам выпуска')
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
    for i, elem in enumerate(names):
        print(f'Название: {elem},  Год выпуска: {years[i]}')


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


names = ["Изучаем Python", "Простой Python", "Django 2 в примерах", "Грокаем алгоритмы",
         "Python. Разработка на основе тестирования"]
years = [2019, 2021, 2019, 2022, 2018]
menu_list()

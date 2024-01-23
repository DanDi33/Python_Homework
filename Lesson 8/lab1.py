def basketball():
    print('\n\t"Великие баскетболисты"\n\n\t'
          '1. Вывести список\n\t'
          '2. Добавить баскетболиста\n\t'
          '3. Удалить баскетболиста\n\t'
          '4. Найти баскетболиста\n\t'
          '5. Заменить данные баскетболиста\n\t')
    match input('Введите число: '):
        case "1":
            show_all(stars)
        case "2":
            add_player(stars)
        case "3":
            del_player(stars)
        case "4":
            search_player(stars)
        case "5":
            change_player(stars)
        case _:
            print("\n\tНекорректный ввод")
    if input("\n\tПерейти в главное меню(y/n)? ") == "y":
        basketball()


def show_all(arr):
    print()
    [print(f"\tИмя - {name}, рост - {value}см") for name, value in arr.items()]


def add_player(arr):
    name = input("\n\tВведите имя и фамилию игрока: ")
    if name not in arr:
        arr[name] = height_of_person()
        print("\tИгрок добавлен.")
    else:
        print("\tИгрок с таким именем существует.")
        if input("\n\tХотите ввести игрока еще раз(y/n)? ") == "y":
            add_player(arr)


def del_player(arr):
    name = input("\n\tВведите имя и фамилию игрока для удаления: ")
    if name in arr:
        arr.pop(name)
        print("\tИгрок удален.")
    else:
        print("\tИгрока с таким именем нет в словаре.")
        if input("\n\tХотите ввести игрока еще раз(y/n)? ") == "y":
            del_player(arr)


def search_player(arr):
    name = input("\n\tВведите имя и фамилию игрока: ")
    if name in arr:
        print(f"\n\tИмя - {name}, рост - {arr[name]}см")
    else:
        print("\tИгрока с таким именем нет в словаре.")
        if input("\n\tХотите ввести игрока еще раз(y/n)? ") == "y":
            search_player(arr)


def change_player(arr):
    name = input("\n\tВведите имя и фамилию игрока, которого хотите заменить: ")
    if name in arr:
        print("\n\tЧто вы хотите заменить?\n\t"
              "1. Имя и фамилию\n\t"
              "2. Рост\n\t"
              "3. Имя, фамилию и рост\n\t")
        match input("\tВведите число: "):
            case "1":
                new_name = input("\n\tВведите имя и фамилию игрока: ")
                if new_name not in arr:
                    arr[new_name] = arr[name]
                    arr.pop(name)
                    print("\tИмя изменено")
                else:
                    print("\tИгрок не заменен.Такое имя существует")
                if input("\n\tХотите заменить игрока еще раз(y/n)? ") == "y":
                    change_player(arr)

            case "2":
                arr[name] = height_of_person()
                print("\tРост изменен")
            case "3":
                new_name = input("\n\tВведите имя и фамилию игрока: ")
                if new_name not in arr:
                    arr[new_name] = height_of_person()
                    arr.pop(name)
                    print("\tИгрок заменен.")
                else:
                    print("\tИгрок не заменен.Такое имя существует")
                    if input("\n\tХотите заменить игрока еще раз(y/n)? ") == "y":
                        change_player(arr)
            case _:
                if input("\n\tВы ввели некорректное значение. Повторить замену(y/n)") == "y":
                    change_player(arr)
    else:
        print("\tИгрока с таким именем нет в словаре.")
        if input("\n\tХотите ввести игрока еще раз(y/n)? ") == "y":
            change_player(arr)


def height_of_person():
    try:
        return int(input("\tВведите рост: "))
    except:
        print("Некорректное значение. Используйте только цифры")
        return height_of_person()


stars = {"Майкл Джордан": 198, "Мэджик Джонсон": 208, "d d": 111, "s s": 222}
basketball()

def company():
    print('\n\t"Коллектив фирмы"\n\n\t'
          '1. Вывести состав\n\t'
          '2. Добавить сотрудника\n\t'
          '3. Удалить сотрудника\n\t'
          '4. Найти сотрудника\n\t'
          '5. Заменить данные сотрудника\n\t')
    match input('\tВведите число: '):
        case "1":
            show_all(team)
        case "2":
            add_worker(team)
        case "3":
            del_worker(team)
        case "4":
            search_worker(team)
        case "5":
            change_worker(team)
        case _:
            print("\n\tНекорректный ввод.")

    if input("\n\tПерейти в главное меню(y/n)? ") == "y":
        company()


def show_all(arr):
    print()
    for el in arr:
        [print(f"{key}: {value}", end=", ") for key, value in el.items()]
        print()


def add_worker(arr):
    worker = input("\n\tВведите ФИО сотрудника: ")
    check = False
    for el in arr:
        if el["name"] == worker:
            check = True
    if check:
        print("\tСотрудник с таким ФИО уже существует в списке сотрудников.")
        if input("\n\t Добавить(y/n)? ") == "y":
            arr.append(create_worker(worker))
            print("\tСотрудник добавлен.")
        else:
            print("\tСотрудник не добавлен в список.")
    else:
        arr.append(create_worker(worker))
        print("\tСотрудник добавлен.")


def create_worker(fio):
    obj_worker = {"name": fio,
                  "phone_number": input("Введите номер телефона: "),
                  "email": input("Введите e-mail: "),
                  "position": input("Введите должность: "),
                  "num_of_room": input("Введите номер кабинета: "),
                  "skype": input("Введите Skype: ")}
    return obj_worker


def del_worker(arr):
    worker = input("\n\tВведите ФИО сотрудника: ")
    check_index = []
    for i in range(len(arr)):
        if arr[i]["name"] == worker:
            check_index.append(i)
            print(f"Индекс - {i}", end=", ")
            [print(f"{key}: {value}", end=", ") for key, value in arr[i].items()]
            print()
    if len(check_index) == 1:
        arr.pop(check_index[0])
        print("\n\tРаботник удален из списка.")
    elif len(check_index) > 1:
        print("\n\tУдалить: "
              f"\n\t1. Одного работника с именем {worker}"
              f"\n\t2. Всех работников с именем {worker}")
        match int(input("\n\tВведите число: ")):
            case 1:
                print("\n\tВыберите индекс для удаления")
                arr.pop(del_index(check_index))
                print("\n\tРаботник удален из списка.")
            case 2:
                for i in range(len(check_index) - 1, -1, -1):
                    arr.pop(check_index[i])
                print("\n\tРаботники удалены из списка.")
            case _:
                print("\n\tНекорректный ввод.")
                del_worker(arr)


def del_index(arr_del_indexes):
    try:
        choosed_index = int(input("\n\tВведите индекс: "))
        if choosed_index in arr_del_indexes:
            return choosed_index
        else:
            print("\n\tНекорректный ввод.")
            return del_index(arr_del_indexes)
    except:
        return del_index(arr_del_indexes)


def search_worker(arr):
    worker = input("\n\tВведите ФИО сотрудника: ")
    check_index = []
    for i in range(len(arr)):
        if arr[i]["name"] == worker:
            check_index.append(i)
    if len(check_index) != 0:
        for el in check_index:
            [print(f"{key}: {value}", end=", ") for key, value in arr[el].items()]
            print()
    else:
        print("\n\tДанного сотрудника нет в списке фирмы.")



def change_worker(arr):
    worker = input("\n\tВведите ФИО сотрудника, которого хотите заменить: ")
    check_index = []
    for i in range(len(arr)):
        if arr[i]["name"] == worker:
            check_index.append(i)
            print(f"Индекс - {i}", end=", ")
            [print(f"{key}: {value}", end=", ") for key, value in arr[i].items()]
            print()
    if len(check_index) == 1:
        arr.append(change_data_worker(arr[check_index[0]]))
        arr.pop(check_index[0])
        print("\n\tДанные сотрудника изменены.")
    elif len(check_index) > 1:
        print("\n\tВыберете сотрудника для изменения: ")
        choosed_index = del_index(check_index)
        arr.append(change_data_worker(arr[choosed_index]))
        arr.pop(choosed_index)
        print("\n\tДанные сотрудника изменены.")
    else:
        print("\tСотрудника с таким ФИО нет в коллективе фирмы")
        if input("\n\tХотите ввести ФИО еще раз(y/n)? ") == "y":
            change_worker(arr)


def change_data_worker(worker):
    print("\n\tЧто вы хотите заменить?\n\t"
          "1. ФИО\n\t"
          "2. Номер телефона\n\t"
          "3. E-mail\n\t"
          "4. Должность\n\t"
          "5. Номер кабинета\n\t"
          "6. Skype\n\t"
          "7. Все данные\n\t")
    match input("\tВведите число: "):
        case "1":
            worker["name"] = input("\n\tВведите ФИО сотрудника: ")
        case "2":
            worker["phone_number"] = input("\n\tВведите номер телефона: ")
        case "3":
            worker["email"] = input("\n\tВведите e-mail: ")
        case "4":
            worker["position"] = input("\n\tВведите должность сотрудника: ")
        case "5":
            worker["num_of_room"] = input("\n\tВведите номер кабинета: ")
        case "6":
            worker["skype"] = input("\n\tВведите skype: ")
        case "7":
            return create_worker(input("\n\tВведите ФИО сотрудника: "))
        case _:
            print("\n\tНекорректный ввод.")
            return change_data_worker(worker)
    return worker


team = [{"name": "Иванов Иван Иванович",
         "phone_number": "+79009001111",
         "email": "ivanovii@team.ru",
         "position": "директор",
         "num_of_room": "1",
         "skype": "123"},
        {"name": "Иванов Петр Петрович",
         "phone_number": "+79009002222",
         "email": "ivanovpp@team.ru",
         "position": "грузчик",
         "num_of_room": "2",
         "skype": "234"},
        {"name": "Петров Иван Петрович",
         "phone_number": "+79009003333",
         "email": "petrovip@team.ru",
         "position": "менеджер",
         "num_of_room": "3",
         "skype": "345"}]
company()

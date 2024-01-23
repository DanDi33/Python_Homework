import os
import pickle


def first():
    file_name = start()
    if file_name is not None:
        main_menu(file_name)
    else:
        first()


def start():
    print("\n\t\"Сотрудники\"\n")
    print("1. Создать файл сотрудников\n"
          "2. Загрузить файл сотрудников\n")
    match input("Введите число: "):
        case "1":
            if not os.path.isdir('data'):
                os.mkdir('data')
            os.chdir('data')
            return create_file()
        case "2":
            newfile = input("Введите файл с расширением для загрузки или путь с полным именем файла: ")
            try:
                with open(newfile, 'rb') as file:
                    print(f"Файл \"{os.path.basename(file.name)}\" загружен")
                    return newfile
            except FileNotFoundError:
                print(f"Запрашиваемый файл \"{newfile}\" не найден")
                return None
        case _:
            print("Некорректное значение")
            return None


def create_file():
    newfile = input("Создать файл с именем: ")
    if "." not in newfile:
        newfile += ".dat"
    if newfile not in os.listdir():
        try:
            with open(newfile, 'wb') as file:
                pickle.dump([], file)
                print(f"файл \"{newfile}\" создан")
            return newfile
        except:
            print("Ошибка 1 создания файла в функции Create_file")
    else:
        print("Файл с таким именем существует.")
        if input("Всё равно хотите создать файл(данные в файле будут утеряны)(y/n)?") == "y":
            try:
                with open(newfile, 'wb') as file:
                    pickle.dump([], file)
                    print(f"файл \"{newfile}\" создан")
                return newfile
            except:
                print("Ошибка 2 создания файла в функции Create_file")
        else:
            return create_file()


def main_menu(newfile):
    print("\n\t\"Сотрудники\"\n\n"
          "1. Ввод данные сотрудника\n"
          "2. Редактирование данных сотрудника\n"
          "3. Удаление сотрудника\n"
          "4. Поиск сотрудника\n"
          "5. Вывод информации обо всех сотрудниках\n"
          "6. Выход\n")
    match input("Введите число: "):
        case "1":
            add_worker(newfile)
        case "2":
            change_worker(newfile)
        case "3":
            delete_worker(newfile)
        case "4":
            find_worker(newfile)
        case "5":
            show_all(newfile)
        case "6":
            print("")
        case _:
            print("Некорректный ввод")
    if input('Хотите вернуться в главное меню(y/n)?') == "y":
        main_menu(newfile)


def add_worker(filename):
    try:
        with open(filename, "rb") as file:
            new = pickle.load(file)
            # print(new)
    except:
        print("Ошибка в функции add_worker при открытии файла.")
    try:
        with open(filename, "wb") as file:
            person = dict()
            person["soname"] = input("Введите фамилию: ")
            person["age"] = int(input("Введите возраст: "))
            new.append(person)
            pickle.dump(new, file)
    except:
        print("Ошибка в функции add_worker при записи файла.")


def change_worker(filename):
    try:
        with open(filename, "rb") as file:
            new = pickle.load(file)
            # print(new)
            founded_person = input("Введите фамилию сотрудника, данные которого вы хотите изменить: ")

        with open(filename, "wb") as file:
            change_worker_before_open(new, founded_person)
            pickle.dump(new, file)
    except:
        print("Ошибка в функции change_worker.")


def change_worker_before_open(arr, f_person):
    check = False
    for i in range(len(arr)):
        if arr[i]["soname"] == f_person:
            check = True
            print("Какие данные Вы хотите изменить?\n"
                  "1. Фамилию\n"
                  "2. Возраст\n"
                  "3. Фамилию и возраст\n")
            match input("Введите число: "):
                case "1":
                    arr[i]["soname"] = input("Введите новую фамилию:")
                case "2":
                    arr[i]["age"] = input("Введите возраст: ")
                case "3":
                    arr[i]["soname"], arr[i]["age"] = input("Введите новую фамилию:"), input("Введите возраст: ")
                case _:
                    print("Некорректный ввод")
                    change_worker_before_open(arr, f_person)
    if not check:
        print("Такого сотрудника нет.")


def find_worker(filename):
    result_for_save = []
    try:
        with open(filename, "rb") as file:
            new = pickle.load(file)
    except IOError:
        print("Ошибка 1 в функции delete_worker.")
    print("Искать сотрудников по ...?\n"
          "1. Фамилии\n"
          "2. Возрасту\n")
    match input("Введите число: "):
        case "1":
            founded_person = input("Введите фамилию сотрудника целиком или частично: ")
            len_word = len(founded_person)
            find_index = []
            for i in range(len(new)):
                if new[i]["soname"][:len_word] == founded_person:
                    find_index.append(i)
                    result_for_save.append(new[i])
            [print(f"Фамилия: {new[index]["soname"]}, возраст: {new[index]["age"]}") for index in find_index]
            if len(find_index) == 0:
                print("Сотрудника с такой фамилией нет.")
        case "2":
            founded_age = int(input("Введите возраст: "))
            find_index = []
            for i in range(len(new)):
                if new[i]["age"] == founded_age:
                    find_index.append(i)
                    result_for_save.append(new[i])
            [print(f"Фамилия: {new[index]["soname"]}, возраст: {new[index]["age"]}") for index in find_index]
            if len(find_index) == 0:
                print("Сотрудника такого возраста нет.")
        case _:
            print("Некорректный ввод")
            find_worker(filename)
    if input("Сохранить данные в файл?") == "y":
        save_to_file(result_for_save)


def save_to_file(result):
    os.chdir('data')
    save_filename = input("Введите имя файла:")
    if "." not in save_filename:
        save_filename += ".dat"
    if save_filename not in os.listdir():
        try:
            with open(save_filename, 'wb') as file:
                pickle.dump(result, file)
                print(f"файл \"{save_filename}\" создан")
        except:
            print("Ошибка 1 создания файла в функции save_to_file")
    else:
        print("Файл с таким именем существует.")
        if input("Всё равно хотите записать данные в файл(данные в файле будут утеряны)(y/n)?") == "y":
            try:
                with open(save_filename, 'wb') as file:
                    pickle.dump(result, file)
                    print(f"файл \"{save_filename}\" создан")
            except:
                print("Ошибка 2 создания файла в функции save_to_file")
        else:
            save_to_file(result)


def delete_worker(filename):
    try:
        with open(filename, "rb") as file:
            new = pickle.load(file)
            # print(new)
            founded_person = input("Введите фамилию сотрудника, данные которого вы хотите удалить: ")

        with open(filename, "wb") as file:
            plan_to_delete_index = []

            for i in range(len(new)):
                if new[i]["soname"] == founded_person:
                    plan_to_delete_index.append(i)

            if len(plan_to_delete_index) == 0:
                print("Такого сотрудника нет.")
            elif len(plan_to_delete_index) == 1:
                new.pop(plan_to_delete_index[0])
                print(f"Сотрудник с фамилией \"{founded_person}\" удален.")
            else:
                show_founded_to_delete_workers(new, plan_to_delete_index)
                del_more_one_workers(new, plan_to_delete_index, founded_person)
            pickle.dump(new, file)
    except IOError:
        print("Ошибка в функции delete_worker.")


def show_founded_to_delete_workers(arr, founded_del_index):
    [print(f"Индекс: {index}, "
           f"фамилия: {arr[index]["soname"]}, "
           f"возраст: {arr[index]["age"]}") for index in founded_del_index]


def del_more_one_workers(arr, founded_del_index, founded_soname):
    founded_del_index = founded_del_index[::-1]
    select_num(arr, founded_del_index, founded_soname)


def select_num(arr, founded_del_index, founded_soname):
    print(f"\nПо Вашему запросу с фамилией - {founded_soname}, найдено сотрудников - {len(founded_del_index)} чел.\n"
          "1. Удалить сотрудника по индексу.\n"
          "2. Удалить всех найденных сотрудников")
    match input("Введите число: "):
        case "1":
            del_by_index(arr, founded_del_index)
        case "2":
            [arr.pop(i) for i in founded_del_index]
            print("Сотрудники удалены")
        case _:
            print("\nНекорректный ввод\n")
            select_num(arr, founded_del_index, founded_soname)


def del_by_index(arr, founded_del_index):
    show_founded_to_delete_workers(arr, founded_del_index)
    index = int(input("Введите индекс для удаления: "))
    if index in founded_del_index:
        arr.pop(index)
        print("Сотрудник удален")
    else:
        print("\nНекорректный ввод\n")
        del_by_index(arr, founded_del_index)


def show_all(filename):
    try:
        with open(filename, "rb") as file:
            data = pickle.load(file)
            [print(f"Фамилия: {person["soname"]}, возраст: {person["age"]}") for person in data]
    except IOError:
        print("Ошибка чтения файла в функции show_all")


if __name__ == '__main__':
    first()

# add_worker('data/list.dat')
# change_worker('data/list.dat')
# delete_worker('data/list.dat')

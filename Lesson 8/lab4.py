def book_collection():
    print('\n\t"Книжная коллекция"\n\n\t'
          '1. Вывести список книг\n\t'
          '2. Добавить книгу\n\t'
          '3. Удалить книгу\n\t'
          '4. Найти книгу\n\t'
          '5. Заменить данные о книге\n\t')
    match input('\tВведите число: '):
        case "1":
            show_all(books)
        case "2":
            add_book(books)
        case "3":
            del_book(books)
        case "4":
            search_book(books)
        case "5":
            change_book(books)
        case _:
            print("\n\tНекорректный ввод.")

    if input("\n\tПерейти в главное меню(y/n)? ") == "y":
        book_collection()


def show_all(arr):
    print()
    for el in arr:
        [print(f"{key}: {value}", end=", ") for key, value in el.items()]
        print()


def add_book(arr):
    book = input("\n\tВведите название книги: ")
    check = False
    for el in arr:
        if el["book"] == book:
            check = True
    if check:
        print("\tКнига с таким названием уже существует в коллекции.")
        if input("\n\t Добавить(y/n)? ") == "y":
            arr.append(create_book(book))
            print("\tКнига добавлена.")
        else:
            print("\tКнига не добавлена в список.")
    else:
        arr.append(create_book(book))
        print("\tКнига добавлена.")


def create_book(name):
    obj_worker = {"author": input("Введите автора книги: "),
                  "book": name,
                  "genre": input("Введите жанр книги: "),
                  "year": input("Введите год выпуска: "),
                  "num_of_pages": input("Введите количество страниц: "),
                  "publisher": input("Введите издательство: ")}
    return obj_worker


def del_book(arr):
    book = input("\n\tВведите название книги: ")
    check_index = []
    for i in range(len(arr)):
        if arr[i]["book"] == book:
            check_index.append(i)
            print(f"Индекс - {i}", end=", ")
            [print(f"{key}: {value}", end=", ") for key, value in arr[i].items()]
            print()
    if len(check_index) == 1:
        arr.pop(check_index[0])
        print("\n\tКнига удалена из списка.")
    elif len(check_index) > 1:
        print("\n\tУдалить: "
              f"\n\t1. Одну книгу с названием - {book}"
              f"\n\t2. Все книги с названием {book}")
        match int(input("\n\tВведите число: ")):
            case 1:
                print("\n\tВыберите индекс для удаления")
                arr.pop(del_index(check_index))
                print("\n\tКнига удалена из списка.")
            case 2:
                for i in range(len(check_index) - 1, -1, -1):
                    arr.pop(check_index[i])
                print("\n\tКниги удалены из списка.")
            case _:
                print("\n\tНекорректный ввод.")
                del_book(arr)


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


def search_book(arr):
    book = input("\n\tВведите название книги: ")
    check_index = []
    for i in range(len(arr)):
        if arr[i]["book"] == book:
            check_index.append(i)
    if len(check_index) != 0:
        for el in check_index:
            [print(f"{key}: {value}", end=", ") for key, value in arr[el].items()]
            print()
    else:
        print("\n\tДанной книги нет в списке.")
        if input("\n\tХотите ввести название книги еще раз(y/n)? ") == "y":
            search_book(arr)


def change_book(arr):
    book = input("\n\tВведите название книги, данные которой хотите изменить: ")
    check_index = []
    for i in range(len(arr)):
        if arr[i]["book"] == book:
            check_index.append(i)
            print(f"Индекс - {i}", end=", ")
            [print(f"{key}: {value}", end=", ") for key, value in arr[i].items()]
            print()
    if len(check_index) == 1:
        arr.append(change_data_book(arr[check_index[0]]))
        arr.pop(check_index[0])
        print("\n\tОписание книги изменено.")
    elif len(check_index) > 1:
        print("\n\tВыберете книгу для изменения: ")
        choosed_index = del_index(check_index)
        arr.append(change_data_book(arr[choosed_index]))
        arr.pop(choosed_index)
        print("\n\tОписание книги изменено.")
    else:
        print("\tКниги с таким названием нет в коллекции")
        if input("\n\tХотите название книги еще раз(y/n)? ") == "y":
            change_book(arr)


def change_data_book(book):
    print("\n\tЧто вы хотите изменить?\n\t"
          "1. Автора\n\t"
          "2. Название\n\t"
          "3. Жанр\n\t"
          "4. Год выпуска\n\t"
          "5. Количество страниц\n\t"
          "6. Издание\n\t"
          "7. Все данные\n\t")
    match input("\tВведите число: "):
        case "1":
            book["author"] = input("\n\tВведите автора: ")
        case "2":
            book["book"] = input("\n\tВведите название книги: ")
        case "3":
            book["genre"] = input("\n\tВведите жанр: ")
        case "4":
            book["year"] = input("\n\tВведите год выпуска: ")
        case "5":
            book["num_of_pages"] = input("\n\tВведите количество страниц: ")
        case "6":
            book["publisher"] = input("\n\tВведите издательство: ")
        case "7":
            return create_book(input("\n\tВведите название книги: "))
        case _:
            print("\n\tНекорректный ввод.")
            return change_data_book(book)
    return book


books = [{"author": "Лутц Марк",
          "book": "Изучаем Python",
          "genre": "Научная литература",
          "year": "2019",
          "num_of_pages": "832",
          "publisher": "Вильямс"},
         {"author": "Персиваль Гарри",
          "book": "Python. Разработка на основе тестирования",
          "genre": "Научная литература",
          "year": "2018",
          "num_of_pages": "622",
          "publisher": "ДМК Пресс"},
         {"author": "Лусиану Рамальо",
          "book": "PYTHON. К вершинам мастерства.",
          "genre": "Научная литература",
          "year": "2022",
          "num_of_pages": "898",
          "publisher": "ДМК Пресс"}]
book_collection()

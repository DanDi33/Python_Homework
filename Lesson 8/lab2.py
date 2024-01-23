def eng_rus_dict():
    print('\n\t"Англо-русский словарь"\n\n\t'
          '1. Вывести все слова\n\t'
          '2. Добавить слово\n\t'
          '3. Удалить слово\n\t'
          '4. Найти слово\n\t'
          '5. Заменить слово\n\t')
    match input('\tВведите число: '):
        case "1":
            show_all(english_dictionary)
        case "2":
            add_word(english_dictionary)
        case "3":
            del_word(english_dictionary)
        case "4":
            search_word(english_dictionary)
        case "5":
            change_word(english_dictionary)
        case _:
            print("\n\tНекорректный ввод")
    if input("\n\tПерейти в главное меню(y/n)? ") == "y":
        eng_rus_dict()


def show_all(arr):
    print()
    [print(f"\t{name} - {value}") for name, value in arr.items()]


def add_word(arr):
    word = input("\n\tВведите введите слово на английском: ")
    if word not in arr:
        arr[word] = input("\tВведите слово на русском: ")
        print("\tСлово добавлено.")
    else:
        print("\tТакое слово уже есть в словаре.")
        if input("\n\tХотите ввести слово еще раз(y/n)? ") == "y":
            add_word(arr)


def del_word(arr):
    word = input("\n\tВведите слово для удаления на английском: ")
    if word in arr:
        arr.pop(word)
        print("\tСлово удален.")
    else:
        print("\tТакого слова нет в словаре.")
        if input("\n\tХотите ввести слово еще раз(y/n)? ") == "y":
            del_word(arr)


def search_word(arr):
    word = input("\n\tВведите слово на английском: ")
    if word in arr:
        print(f"\n\t{word} - {arr[word]}")
    else:
        print("\tТакого слова нет в словаре.")
        if input("\n\tХотите ввести слово еще раз(y/n)? ") == "y":
            search_word(arr)


def change_word(arr):
    word = input("\n\tВведите слово на английском, которого хотите заменить: ")
    if word in arr:
        print("\n\tЧто вы хотите заменить?\n\t"
              "1. Слово на английском\n\t"
              "2. Перевод на русском\n\t"
              "3. Оба слова\n\t")
        match input("\tВведите число: "):
            case "1":
                new_word = input("\n\tВведите слово на английском: ")
                if new_word not in arr:
                    arr[new_word] = arr[word]
                    arr.pop(word)
                    print("\tСлово изменено")
                else:
                    print("\tСлово не заменено.Такое слово существует в словаре")
                if input("\n\tХотите заменить слово еще раз(y/n)? ") == "y":
                    change_word(arr)

            case "2":
                arr[word] = input("\n\tВведите новый перевод: ")
                print("\tСлово изменено")
            case "3":
                new_word = input("\n\tВведите слово на английском: ")
                if new_word not in arr:
                    arr[new_word] = input("\n\tВведите новый перевод: ")
                    arr.pop(word)
                    print("\tСлово заменено.")
                else:
                    print("\tСлово не заменено.Такое слово существует в словаре")
                    if input("\n\tХотите заменить слово еще раз(y/n)? ") == "y":
                        change_word(arr)
            case _:
                if input("\n\tВы ввели некорректное значение. Повторить замену(y/n)") == "y":
                    change_word(arr)
    else:
        print("\tТакого слова нет в словаре.")
        if input("\n\tХотите ввести слово еще раз(y/n)? ") == "y":
            change_word(arr)


english_dictionary = {"teacher": "учитель",
                      "player": "игрок",
                      "pen": "ручка"}
eng_rus_dict()

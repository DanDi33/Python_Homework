def show_code_or_text():
    print("\n\tПрограмма кодирования текста с помощью клавиатуры кнопочного телефона\n\t")
    # ОТКАЗАЛСЯ ОТ ОБРАТНОГО ДЕКОДИРОВАНИЯ, ТАК КАК НЕВОЗМОЖНО ОПРЕДЕЛИТЬ БУКВЫ, ЕСЛИ ОНИ 2 ИЛИ БОЛЕЕ РАЗ ПОДРЯД
    # ПОПАДАЮ НА ОДИН КЛЮЧ
    # "1. Закодировать текст.\n\t"
    # "2. Декодировать текст\n\t")
    # match input("\tВведите число: "):
    #   case "1":
    #       print()
    new_syms = new_dict()
    text = input("\tВведите текст(латинские буквы и некоторые знаки препинания): ")
    # text = "Hell&o, Worl@d"
    print("\tВаш текст: ", text)
    arr = get_arr_cleared(text, "abcdefghijklmnopqrstuvwxyz.,?!: ")
    print("\tВаш очищенный текст: ", "".join(arr))
    print(f"\tВаш код:", end=" ")
    [print(new_syms[el.lower()], end="") for el in arr]
    print()
        # case "2":
        #     str_sym = input("\n\tВведите код(только цифры): ")
        #     # str_sym = "443355 555f5666110966d677755531111"
        #     print("\n\tВаш код: ", str_sym)
        #     arr = get_arr_cleared(str_sym, "1234567890")
        #     print("\tВаш очищенный код: ", "".join(arr))
        #     phone_keys = phone_keyboard()
        #     count = 0
        #     prev = arr[0]
        #     print(f"\tВаш текст:", end=" ")
        #     for i in range(1, len(arr)):
        #         if arr[i] != prev:
        #             print(phone_keys[prev][count], end="")
        #             count = 0
        #         else:
        #             count += 1
        #             len_cort = len(phone_keys[arr[i]])
        #             if i == len(arr) - 1:
        #                 count += 1
        #                 len_cort = count
        #             if count == len_cort:
        #                 print(phone_keys[prev][count - 1], end="")
        #                 count = 0
        #         prev = arr[i]
        #     print()
        # case _:
        #     print("\n\tНекорректный ввод")
        #     if input("\n\tХотите вернуться в меню(y/n)? ") == "y":
        #         show_code_or_text()


def phone_keyboard():
    return {"1": (".", ",", "?", "!", ":"),
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z"),
            "0": " "}


def new_dict():  # функция преобразует словарь "клавиатура телефона", в словарь в котором в ключах - алфавит и знаки
    # припинания, а в значениях - цифры соответствующие по нажатиям данному символу
    symbols = phone_keyboard()
    new_symbs = {}
    for key, value in symbols.items():
        for i in range(len(value)):
            new_symbs[value[i]] = key * (i + 1)
    return new_symbs


def get_arr_cleared(str, arr_rule):  # функция очищает текст от "лишних" символов и преобразует его в массив
    arr = [el for el in str]
    for i in range(len(arr) - 1, -1, -1):
        if arr[i].lower() not in arr_rule:
            arr.pop(i)
    return arr


show_code_or_text()

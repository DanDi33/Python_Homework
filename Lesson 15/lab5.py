def show_menu(func):
    def wrapper(s):
        res = func(s)
        [print(f"{index+1}. {word.title()}") for index, word in enumerate(res)]
    return wrapper


@show_menu
def get_menu(s):
    return s.split()


get_menu("Начало середина конец")


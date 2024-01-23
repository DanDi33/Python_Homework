def func_show(func):
    def wrapper(width, height):
        print(f"Площадь прямоугольника: {func(width, height)}")

    return wrapper


@func_show
def get_sq(width, height):
    return width * height


get_sq(3, 4)

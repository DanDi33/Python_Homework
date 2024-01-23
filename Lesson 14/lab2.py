# Создайте класс для конвертирования температуры из
# Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фа-
# ренгейт и для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температуры и
# возвращать это значение с помощью статического метода.
class Degrees:
    counter = 0

    @staticmethod
    def cel_to_far(value):
        Degrees.counter += 1
        if isinstance(value, int):
            return value * 1.8 + 32
        else:
            return f"Некорректный формат"

    @staticmethod
    def far_to_cel(value):
        Degrees.counter += 1
        if isinstance(value, int):
            return (value - 32) / 1.8
        else:
            return f"Некорректный формат"

    @staticmethod
    def show_counter():
        return Degrees.counter


dt = Degrees()
print(dt.cel_to_far(10))
print(dt.__dict__)
print(dt.show_counter())
dt2 = Degrees()
print(dt2.far_to_cel(100))
print(dt2.__dict__)
print(dt2.show_counter())

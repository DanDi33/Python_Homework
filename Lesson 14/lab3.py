# Создайте класс для перевода из метрической системы
# в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно
# реализуйте перевод мер длины.
# Дюйм (inch) = 25,4 мм (2,54 см).
# Фут (foot) = 0,3048 м (или 12 дюймов).
# Ярд (yard) = 0,9144 м (или 3 фута).
# Миля (mile) = 1,609 км (или 1,760 ярда).
# Хэнд (hand) = 10,16 см (или 4 дюйма).
class MathEnglishSys:
    @staticmethod
    def inch_to_sm(value):
        if isinstance(value, int):
            return value * 2.54
        else:
            return f"Некорректный формат"

    @staticmethod
    def sm_to_inch(value):
        if isinstance(value, int):
            return value / 2.54
        else:
            return f"Некорректный формат"

    @staticmethod
    def foot_to_m(value):
        if isinstance(value, int):
            return value * 0.3048
        else:
            return f"Некорректный формат"

    @staticmethod
    def m_to_foot(value):
        if isinstance(value, int):
            return value / 0.3048
        else:
            return f"Некорректный формат"

    @staticmethod
    def yard_to_m(value):
        if isinstance(value, int):
            return value * 0,9144
        else:
            return f"Некорректный формат"

    @staticmethod
    def m_to_yard(value):
        if isinstance(value, int):
            return value / 0,9144
        else:
            return f"Некорректный формат"


sm = MathEnglishSys()
print(sm.inch_to_sm(5))
print(sm.inch_to_sm("a5"))
print(sm.sm_to_inch(254))
print(sm.foot_to_m(10))
print(sm.foot_to_m("10"))
print(sm.m_to_foot(100))

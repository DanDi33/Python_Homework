class Figure:
    def __init__(self, name):
        self.name = name

    def get_area(self):
        return 0

    def __str__(self):
        return f'Фигура - {self.name}, площадь: {self.get_area()}'


class Rectangle(Figure):
    """Прямоугольник. Конструктор принимает длину и ширину"""

    def __init__(self, a, b):
        super().__init__('прямоугольник')
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class RightTriangle(Figure):
    """Прямоугольный треугольник. Конструктор принимает длины катетов"""

    def __init__(self, leg_1, leg_2):
        super().__init__('прямоугольный треугольник')
        self.leg_1 = leg_1
        self.leg_2 = leg_2

    def get_area(self):
        return self.leg_1 * self.leg_2 / 2


class Circle(Figure):
    """Круг. Конструктор принимает радиус"""

    def __init__(self, radius):
        super().__init__('круг')
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius


r = Rectangle(10, 20)
print(r)
c = Circle(5)
print(c)
tr = RightTriangle(4, 5)
print(tr)


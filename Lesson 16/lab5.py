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
        self.area = self.a * self.b

    def __str__(self):
        return f'Фигура - {self.name}, площадь: {self.area}'


class RightTriangle(Figure):
    """Прямоугольный треугольник. Конструктор принимает длины катетов"""

    def __init__(self, side_1, side_2):
        super().__init__('прямоугольный треугольник')
        self.side_1 = side_1
        self.side_2 = side_2
        self.area = self.side_1 * self.side_2 / 2

    def __str__(self):
        return f'Фигура - {self.name}, площадь: {self.area}'


class Circle(Figure):
    """Круг. Конструктор принимает радиус"""

    def __init__(self, radius):
        super().__init__('круг')
        self.radius = radius
        self.area = 3.14 * self.radius * self.radius

    def __str__(self):
        return f'Фигура - {self.name}, площадь: {self.area}'


r = Rectangle(10, 20)
print(r)
c = Circle(5)
print(c)
tr = RightTriangle(4, 5)
print(tr)

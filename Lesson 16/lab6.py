import pickle
import os


class Shape:
    figures = []

    def __init__(self, name):
        self.name = name

    def show(self):
        pass

    def save(self):
        filename = input("Введите имя файла для сохранения:")
        if "." not in filename:
            filename += ".dat"
        # Если файл существует, модуль считывает данные из файла и записывает в свойство figures.
        # Если модуль убрать, то данные в существующем файле будут удаляться
        if filename in os.listdir():
            try:
                with open(filename, 'rb') as file:
                    Shape.figures = pickle.load(file)
            except:
                print("Ошибка 1 - чтения файла (в методе save класса Shape)")
        # конец модуля
        try:
            with open(filename, 'wb') as file:
                Shape.figures.append(self.__dict__)
                pickle.dump(Shape.figures, file)
                print(f"файл \"{filename}\" сохранен")

        except:
            print("Ошибка 2 - создания файла (в методе save класса Shape)")

    @staticmethod
    def load():
        filename = input("Введите имя файла для загрузки:")
        if "." not in filename:
            filename += ".dat"
        if filename in os.listdir():
            try:
                with open(filename, 'rb') as file:
                    print(f"Файл \"{os.path.basename(file.name)}\" загружен")
                    Shape.figures = pickle.load(file)
            except:
                print("Ошибка 2 - загрузка файла (в методе load класса Shape)")
        else:
            print(f"Запрашиваемый файл \"{filename}\" не найден")

    @staticmethod
    def show_all_figures():
        # [[print(f'{key}: {el}', end=", ") for key, el in elem.items()] for elem in Shape.figures]
        for index, elem in enumerate(Shape.figures):
            print(f"{index + 1}.", end=" ")
            for key, el in elem.items():
                print(f'{key}: {el}', end=", ")
            print()


class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__('Квадрат')
        self.x = x
        self.y = y
        self.side = side

    def show(self):
        print(
            f"Фигура - {self.name}, с координатами верхнего левого угла - x: {self.x}; y: {self.y} и стороной {self.side}")


class Rectangle(Shape):
    def __init__(self, x, y, side1, side2):
        super().__init__('Прямоугольник')
        self.x = x
        self.y = y
        self.side1 = side1
        self.side2 = side2

    def show(self):
        print(
            f"Фигура - {self.name}, с координатами верхнего левого угла - x: {self.x}; y: {self.y} "
            f"и сторонами: {self.side1}, {self.side2}")


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__('Окружность')
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        print(
            f"Фигура - {self.name}, с координатами верхнего левого угла - x: {self.x}; y: {self.y} "
            f"и радиусом {self.radius}")


class Ellipse(Shape):
    def __init__(self, x, y, side1, side2):
        super().__init__('Эллипс')
        self.x = x
        self.y = y
        self.side1 = side1
        self.side2 = side2

    def show(self):
        print(
            f"Фигура - {self.name}, с координатами верхнего левого угла - x: {self.x}; y: {self.y} "
            f"и сторонами: {self.side1}, {self.side2}")


class Triangle(Shape):
    def __init__(self, x, y, katet1, katet2, hypotenuse):
        super().__init__('Треугольник')
        self.x = x
        self.y = y
        self.katet1 = katet1
        self.katet2 = katet2
        self.hypotenuse = hypotenuse

    def show(self):
        print(
            f"Фигура - {self.name}, с координатами верхнего левого угла - x: {self.x}; y: {self.y} "
            f"и сторонами: {self.katet1}, {self.katet2}, {self.hypotenuse}")


kv = Square(1, 2, 3)
kv.show()
kv2 = Square(2, 3, 5)
kv2.show()
re = Rectangle(5, 6, 5, 2)
re.show()
re.save()
ci = Circle(4, 4, 8)
ci.show()
ci.save()
el = Ellipse(2,2,6,7)
el.show()
el.save()
tr = Triangle(3, 4, 3, 4, 5)
tr.show()
tr.save()
kv.save()
print(Shape.figures)
kv2.save()
print(Shape.figures)
kv.load()
print(Shape.figures)
kv.show_all_figures()

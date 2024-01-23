class Car:
    def __init__(self, producer=None, model=None, year=None, engine=None, color=None, cost=None):
        self.producer = producer
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.cost = cost

    def change_producer(self, value):
        self.producer = value

    def change_model(self, value):
        self.model = value

    def change_year(self, value):
        self.year = value

    def change_engine(self, value):
        self.engine = value

    def change_color(self, value):
        self.color = value

    def change_cost(self, value):
        self.cost = value

    def input_data(self):
        print("\n\"Введите данные об автомобиле\"\n")
        self.producer = input(f'Производитель:{"":<28}')
        self.model = input(f'Модель:{"":<35}')
        self.year = int(input(f'Года выпуска:{"":<29}'))
        self.engine = int(input(f'Объемом двигателя(см3):{"":<19}'))
        self.color = input(f'Цвет:{"":<37}')
        self.cost = int(input(f'Стоимость(руб):{"":<27}'))
        print("*" * 45)

    def show_data(self):
        print('\n"Данные автомобиля"\n\n'
              f'Автомобиль(марка, модель):{"":<15} {self.producer} {self.model}\n'
              f'Года выпуска:{"":<28} {self.year}\n'
              f'Объемом двигателя(см3):{"":<18} {self.engine}\n'
              f'Цвет:{"":<36} {self.color}\n'
              f'Стоимость(руб):{"":<26} {self.cost}')


# mers = Car("Mercedes", "E320", 2019, 3200, "белый", 40000)
# mers.show_data()
# bmw = Car()
# bmw.input_data()
# bmw.show_data()
# lada = Car()
# lada.show_data()

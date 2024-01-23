class Car:
    def __init__(self, producer=None, model=None, year=None, engine=None, color=None, cost=None):
        self.producer = producer
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.cost = cost

    def change_producer(self, value):
        if value is not None:
            self.producer = value

    def change_model(self, value):
        if value is not None:
            self.model = value

    def change_year(self, value):
        if value is not None:
            self.year = value

    def change_engine(self, value):
        if value is not None:
            self.engine = value

    def change_color(self, value):
        if value is not None:
            self.color = value

    def change_cost(self, value):
        if value is not None:
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


class ElectroCar(Car):
    def __init__(self, producer=None, model=None, year=None, color=None, range_of_car=None, battery_capacity=None, cost=None):
        super().__init__(producer, model, year, color, cost)
        self.range = range_of_car
        self.battery_capacity = battery_capacity
        self.delete_engine()

    def delete_engine(self):
        delattr(self, 'engine')

    def change_engine(self, value):
        pass

    def change_battery_cap(self, value):
        if value is not None:
            self.battery_capacity = value

    def change_range(self, value):
        if value is not None:
            self.range = value

    def input_data(self):
        print("\n\"Введите данные об автомобиле\"\n")
        self.producer = input(f'Производитель:{"":<28}')
        self.model = input(f'Модель:{"":<35}')
        self.year = int(input(f'Года выпуска:{"":<29}'))
        self.battery_capacity = int(input(f'Ёмкость аккумулятора(А/ч):{"":<16}'))
        self.range = int(input(f'Запас хода(км):{"":<27}'))
        self.color = input(f'Цвет:{"":<37}')
        self.cost = int(input(f'Стоимость(руб):{"":<27}'))
        print("*" * 45)

    def show_data(self):
        print('\n"Данные автомобиля"\n\n'
              f'Автомобиль(марка, модель):{"":<15} {self.producer} {self.model}\n'
              f'Года выпуска:{"":<28} {self.year}\n'
              f'Ёмкость аккумулятора(А/ч):{"":<15} {self.battery_capacity}\n'
              f'Запас хода(км):{"":<26} {self.range}\n'
              f'Цвет:{"":<36} {self.color}\n'
              f'Стоимость(руб):{"":<26} {self.cost}')


# mers = ElectroCar("Mercedes", "E320", 2019, "белый", 500, 100, 40000)
# mers.change_engine(3200)
# mers.show_data()
# print(mers.__dict__)
bmw = ElectroCar()
bmw.input_data()
bmw.show_data()
# lada = Car()
# lada.show_data()

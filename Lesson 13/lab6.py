class Stadium:
    def __init__(self, name=None, date=None, country=None, city=None, capacity=None):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity

    def change_name(self, value):
        if value is not None:
            self.name = value

    def change_date(self, value):
        if value is not None:
            self.date = value

    def change_country(self, value):
        if value is not None:
            self.country = value

    def change_city(self, value):
        if value is not None:
            self.city = value

    def change_capacity(self, value):
        if value is not None:
            self.capacity = value

    def input_data(self):
        print("\n\"Введите данные о стадионе\"\n")
        self.name = input(f'Название стадиона:{"":<25}')
        self.date = input(f'Дата открытия:{"":<29}')
        self.country = input(f'Страна:{"":<36}')
        self.city = input(f'Город:{"":<37}')
        self.capacity = int(input(f'Вместимость:{"":<31}'))
        print("*" * 45)

    def show_data(self):
        print('\n"Данные стадиона"\n\n'
              f'Название стадиона:{"":<24} {self.name}\n'
              f'Дата открытия:{"":<28} {self.date}\n'
              f'Страна:{"":<35} {self.country}\n'
              f'Город:{"":<36} {self.city}\n'
              f'Вместимость:{"":<30} {self.capacity}')


class StadiumOfMoscow(Stadium):
    def __init__(self, name=None, date=None, country=None, city=None, capacity=None, near_metro=None, roof=None):
        super().__init__(name, date, country, city, capacity)
        self.near_metro = near_metro
        self.roof = roof

    def change_near_metro(self, value):
        if value is not None:
            self.near_metro = value

    def change_capacity(self, value):
        if value is not None:
            self.roof = value

    def input_data(self):
        print("\n\"Введите данные о стадионе\"\n")
        self.name = input(f'Название стадиона:{"":<25}')
        self.date = input(f'Дата открытия:{"":<29}')
        self.country = input(f'Страна:{"":<36}')
        self.city = input(f'Город:{"":<37}')
        self.capacity = int(input(f'Вместимость:{"":<31}'))
        self.near_metro = input(f'Ближайшее метро:{"":<27}')
        self.roof = input(f'Наличие крыши:{"":<29}')
        print("*" * 45)

    def show_data(self):
        print('\n"Данные стадиона"\n\n'
              f'Название стадиона:{"":<24} {self.name}\n'
              f'Дата открытия:{"":<28} {self.date}\n'
              f'Страна:{"":<35} {self.country}\n'
              f'Город:{"":<36} {self.city}\n'
              f'Вместимость:{"":<30} {self.capacity}\n'
              f'Ближайшее метро:{"":<26} {self.near_metro}\n'
              f'Наличие крыши:{"":<28} {self.roof}')


# st1 = StadiumOfMoscow("Лужники", "31.07.1956", "СССР", "Москва", 81000, "Лужники", "Да")
# st1.show_data()


st2 = StadiumOfMoscow()
st2.input_data()
st2.show_data()

# st3 = StadiumOfMoscow()
# st3.show_data()
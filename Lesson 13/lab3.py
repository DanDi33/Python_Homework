class Stadium:
    def __init__(self, name=None, date=None, country=None, city=None, capacity=None):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity

    def change_name(self, value):
        self.name = value

    def change_date(self, value):
        self.date = value

    def change_country(self, value):
        self.country = value

    def change_city(self, value):
        self.city = value

    def change_capacity(self, value):
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


st1 = Stadium("Лужники", "31.07.1956", "СССР", "Москва", 81000)
st1.show_data()
# st2 = Stadium()
# st2.input_data()
# st2.show_data()
# st3 = Stadium()
# st3.show_data()

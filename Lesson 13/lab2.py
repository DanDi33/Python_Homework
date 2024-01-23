class Book:
    def __init__(self, title=None, year=None, producer=None, genre=None, author=None, cost=None):
        self.title = title
        self.year = year
        self.producer = producer
        self.genre = genre
        self.author = author
        self.cost = cost

    def change_title(self, value):
        self.title = value

    def change_year(self, value):
        self.year = value

    def change_producer(self, value):
        self.producer = value

    def change_genre(self, value):
        self.genre = value

    def change_author(self, value):
        self.author = value

    def change_cost(self, value):
        self.cost = value

    def input_data(self):
        print("\n\"Введите данные о книге\"\n")
        self.title = input(f'Название книги:{"":<27}')
        self.year = int(input(f'Года выпуска:{"":<29}'))
        self.producer = input(f'Издатель:{"":<33}')
        self.genre = input(f'Жанр:{"":<37}')
        self.author = int(input(f'Автор книги:{"":<30}'))
        self.cost = int(input(f'Стоимость(руб):{"":<27}'))
        print("*" * 45)

    def show_data(self):
        print('\n"Данные книги"\n\n'
              f'Название книги:{"":<26} {self.title}\n'
              f'Года выпуска:{"":<28} {self.year}\n'
              f'Издатель:{"":<32} {self.producer}\n'
              f'Жанр:{"":<36} {self.genre}\n'
              f'Автор книги:{"":<29} {self.author}\n'
              f'Стоимость(руб):{"":<26} {self.cost}')


war_and_peace = Book("Война и Мир", 2020, "ЭКСМО", "классика", "Толстой Л.Н.", 460)
war_and_peace.show_data()
# book2 = Book()
# book2.input_data()
# book2.show_data()
# book3 = Book()
# book3.show_data()

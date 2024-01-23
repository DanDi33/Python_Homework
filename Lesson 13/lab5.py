class Book:
    def __init__(self, title=None, year=None, producer=None, genre=None, author=None, cost=None):
        self.title = title
        self.year = year
        self.producer = producer
        self.genre = genre
        self.author = author
        self.cost = cost

    def change_title(self, value):
        if value is not None:
            self.title = value

    def change_year(self, value):
        if value is not None:
            self.year = value

    def change_producer(self, value):
        if value is not None:
            self.producer = value

    def change_genre(self, value):
        if value is not None:
            self.genre = value

    def change_author(self, value):
        if value is not None:
            self.author = value

    def change_cost(self, value):
        if value is not None:
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


class ChildrenBook(Book):
    def __init__(self, title=None, year=None, producer=None, genre=None, author=None, age_rating=None, pages=None,
                 cost=None):
        super().__init__(title, year, producer, genre, author, cost)
        self.age_rating = age_rating
        self.pages = pages

    def change_rating(self, value):
        if value is not None:
            self.age_rating = value

    def change_pages(self, value):
        if value is not None:
            self.pages = value

    def input_data(self):
        print("\n\"Введите данные о книге\"\n")
        self.title = input(f'Название книги:{"":<27}')
        self.year = int(input(f'Года выпуска:{"":<29}'))
        self.producer = input(f'Издатель:{"":<33}')
        self.genre = input(f'Жанр:{"":<37}')
        self.author = int(input(f'Автор книги:{"":<30}'))
        self.age_rating = int(input(f'Возрастной рейтинг:{"":<23}'))
        self.pages = int(input(f'Количество страниц:{"":<23}'))
        self.cost = int(input(f'Стоимость(руб):{"":<27}'))
        print("*" * 45)

    def show_data(self):
        print('\n"Данные книги"\n\n'
              f'Название книги:{"":<26} {self.title}\n'
              f'Года выпуска:{"":<28} {self.year}\n'
              f'Издатель:{"":<32} {self.producer}\n'
              f'Жанр:{"":<36} {self.genre}\n'
              f'Автор книги:{"":<29} {self.author}\n'
              f'Возрастной рейтинг:{"":<22} {self.age_rating}\n'
              f'Количество страниц:{"":<22} {self.pages}\n'
              f'Стоимость(руб):{"":<26} {self.cost}')


# cat_in_boots = ChildrenBook("Кот в сапогах", 2020, "Лорета", "Сказка", "Шарль Перро", "3+", 48, 651)
# cat_in_boots.show_data()
book2 = ChildrenBook()
book2.input_data()
book2.show_data()
# book3 = Book()
# book3.show_data()

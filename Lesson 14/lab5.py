class Ship:
    def __init__(self, name, type_of_ship, tonnage, speed, power, length, crew):
        self.name = name
        self.type_of_ship = type_of_ship
        self.tonnage = tonnage
        self.speed = speed
        self.power = power
        self.length = length
        self.crew = crew

    def __str__(self):
        return (f'\n\"Данные о корабле\"\n\n'
                f'Название о корабле:{"":<8} {self.name}\n'
                f'Тип судна:{"":<17} {self.type_of_ship}\n'
                f'Водоизмещение:{"":<13} {self.tonnage} т\n'
                f'Скорость:{"":<18} {self.speed} узл\n'
                f'Мощность двигателя:{"":<8} {self.power} л.с.\n'
                f'Длина судна:{"":<15} {self.length} м\n'
                f'Экипаж:{"":<20} {self.crew} чел\n')


class Frigate(Ship):
    """Класс Фрегат. На борту максимум 8 ракет. Может стрелять, перезаряжать и выдавать информацию о количестве
оставшихся ракет и количестве выпущенных"""

    def __init__(self, name, type_of_ship, tonnage, speed, power, length, crew):
        super().__init__(name, type_of_ship, tonnage, speed, power, length, crew)
        self.missiles = 8
        self.launched_missiles = 0

    def launch_missile(self):
        if self.missiles <= 0:
            print(f"Ракеты закончились. Перезарядитесь")
        else:
            print("Выстрел! Ракета ушла. Расход: 1")
            self.missiles -= 1
            self.launched_missiles += 1

    def reload(self):
        self.missiles = 8
        print("Боекомплект пополнен")

    def show_ammunition(self):
        print(f"Остаток ракет: {self.missiles}, расход: {self.launched_missiles}")


class Destroyer(Ship):

    def __init__(self, name, type_of_ship, tonnage, speed, power, length, crew):
        super().__init__(name, type_of_ship, tonnage, speed, power, length, crew)
        self.mines = 20
        self.used_mines = 0

    def laid_mine(self):
        if self.mines <= 0:
            print(f"Мины закончились. Перезарядитесь")
        else:
            print("Сброс! Мина установлена. Расход: 1")
            self.mines -= 1
            self.used_mines += 1

    def reload(self):
        self.mines = 20
        print("Боекомплект пополнен")

    def show_ammunition(self):
        print(f"Остаток мин: {self.mines}, расход: {self.used_mines}")


class Cruiser(Ship):

    def __init__(self, name, type_of_ship, tonnage, speed, power, length, crew):
        super().__init__(name, type_of_ship, tonnage, speed, power, length, crew)
        self.pro_missiles = 15
        self.anti_career_missiles = 6
        self.used_pro_missiles = 0
        self.used_anti_career_missiles = 0

    def launch_pro_missile(self):
        if self.pro_missiles <= 0:
            print(f"Ракеты закончились. Перезарядитесь")
        else:
            print("Выстрел! Ракета ПРО ушла. Расход: 1")
            self.pro_missiles -= 1
            self.used_pro_missiles += 1

    def launch_ac_missile(self):
        if self.anti_career_missiles <= 0:
            print(f"Ракеты закончились. Перезарядитесь")
        else:
            print("Выстрел! Ракета ПК ушла. Расход: 1")
            self.anti_career_missiles -= 1
            self.used_anti_career_missiles += 1

    def reload_pro(self):
        self.pro_missiles = 15
        print("Боекомплект пополнен")

    def reload_ac(self):
        self.anti_career_missiles = 6
        print("Боекомплект пополнен")

    def show_ammunition(self):
        print(f"Остаток ракет ПРО: {self.pro_missiles}, расход: {self.used_pro_missiles}\n"
              f"Остаток ракет ПК: {self.anti_career_missiles}, расход: {self.used_anti_career_missiles}\n")


# knox = Frigate("Knox", "Фрегат", 4163, 27, 35000, 133.5, 244)
# knox2 = Frigate("Knox2", "Фрегат", 4163, 27, 35000, 133.5, 244)
# print(knox)
# knox.launch_missile()
# print(knox2)
# knox2.launch_missile()
# knox2.launch_missile()
# knox.show_ammunition()
# knox2.show_ammunition()
# knox.launch_missile()
# knox.launch_missile()
# knox.show_ammunition()
# knox.launch_missile()
# knox.launch_missile()
# knox.launch_missile()
# knox.launch_missile()
# knox.launch_missile()
# knox.launch_missile()
# knox.show_ammunition()
# knox.reload()
# knox.show_ammunition()
# knox.launch_missile()
# knox.launch_missile()
# knox.show_ammunition()
# print(knox)
# print(knox.__dict__)
# print(Frigate.__dict__)
# print(Frigate.__doc__)

# sarich = Destroyer("Отличный", "Эсминец", 6500, 32, 100000, 145, 344)
# print(sarich)
# sarich.laid_mine()
# sarich.show_ammunition()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.laid_mine()
# sarich.show_ammunition()
# sarich.reload()
# sarich.show_ammunition()
# sarich.laid_mine()
# sarich.show_ammunition()

petr = Cruiser("Петр Великий", "Крейсер", 23750, 32, 140000, 230, 744)
print(petr)
petr.launch_pro_missile()
petr.show_ammunition()
petr.launch_pro_missile()
petr.launch_pro_missile()
petr.launch_pro_missile()
petr.launch_pro_missile()
petr.launch_pro_missile()
petr.launch_pro_missile()
petr.launch_pro_missile()
petr.launch_pro_missile()
petr.launch_pro_missile()
petr.launch_pro_missile()
petr.launch_pro_missile()
petr.launch_pro_missile()
petr.launch_pro_missile()
petr.launch_pro_missile()
petr.launch_pro_missile()
petr.show_ammunition()
petr.reload_pro()
petr.launch_pro_missile()
petr.show_ammunition()
petr.launch_ac_missile()
petr.show_ammunition()
petr.launch_ac_missile()
petr.launch_ac_missile()
petr.launch_ac_missile()
petr.launch_ac_missile()
petr.launch_ac_missile()
petr.launch_ac_missile()
petr.show_ammunition()
petr.reload_ac()
petr.launch_ac_missile()
petr.show_ammunition()

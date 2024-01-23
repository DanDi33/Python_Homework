class Money:
    MIN_coins = 0
    MAX_coins = 100

    def __init__(self, banknote=0, coins=0):
        self.banknote = banknote
        self.coins = coins

    def __str__(self):
        return f"{self.banknote},{self.coins}"

    def get_banknote(self):
        return self.banknote

    def set_banknote(self, value):
        if isinstance(value, int):
            self.banknote = value
        else:
            print("Некорректный ввод")

    def get_coins(self):
        return self.coins

    def set_coins(self, value):
        if isinstance(value, int) and (Money.MIN_coins <= value < Money.MAX_coins):
            self.coins = value
        else:
            print("Некорректный ввод")


class Rub(Money):
    def __init__(self, banknote, coins):
        super().__init__(banknote, coins)

    def __str__(self):
        return f"{self.banknote}руб {self.coins}коп"


class Dollar(Money):
    def __init__(self, banknote, coins):
        super().__init__(banknote, coins)

    def __str__(self):
        return f"{self.banknote}$ {self.coins}¢"


ru = Rub(1, 23)
print(ru.get_banknote())
print(ru.get_coins())
print(ru)
ru.set_banknote(2)
ru.set_coins(12)
print(ru)

dol = Dollar(10, 53)
print(dol.get_banknote())
print(dol.get_coins())
print(dol)
dol.set_banknote(5)
dol.set_coins(62)
print(dol)
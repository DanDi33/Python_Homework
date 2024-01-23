class Fraction:
    count = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.count += 1

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    # def __add__(self, other):
    #     new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
    #     new_denominator = self.denominator * other.denominator
    #     return Fraction(new_numerator, new_denominator)

    @staticmethod
    def get_count():
        return Fraction.count


fraction1 = Fraction(1, 2)
print(fraction1)
print(f"Количество обращений к классу: {Fraction.get_count()}")
fraction2 = Fraction(3, 4)
print(fraction2)
print(f"Количество обращений к классу: {Fraction.get_count()}")
# fraction3 = fraction1 + fraction2
# print(fraction3)
# print(f"Количество обращений к классу: {Fraction.get_count()}")
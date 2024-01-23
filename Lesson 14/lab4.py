class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power


class CoffeeMachine(Device):
    def __init__(self, brand, model, power, cups_per_day):
        super().__init__(brand, model, power)
        self.cups_per_day = cups_per_day

    @staticmethod
    def brew_coffee(coffee_type):
        print(f"Brewing {coffee_type} coffee")


class Blender(Device):
    def __init__(self, brand, model, power, volume):
        super().__init__(brand, model, power)
        self.volume = volume

    @staticmethod
    def blend(ingredient):
        print(f"Blending {ingredient}")


class MeatGrinder(Device):
    def __init__(self, brand, model, power, kilo_per_day):
        super().__init__(brand, model, power)
        self.kilo_per_day = kilo_per_day

    @staticmethod
    def grind_meat(meat_type):
        print(f"Grinding {meat_type} meat")


dev1 = CoffeeMachine("DeLonghi", "123", 1200, 120)
dev1.brew_coffee("Arabica")
dev2 = Blender("Dexp",234,900,1.5)
dev2.blend("Eggs")
dev3 = MeatGrinder("LG",1245,1700,10)
dev3.grind_meat("beef")

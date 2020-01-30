# Bouw de klasse Tesla in Python die in elk geval de volgende eigenschappen bezit:
# • type kan de waarde S, X, 3 of Y hebben
# • color kan de waarde Deep Blue, Midnight Silver, Pearl White, Red, Solid
# Black
# • mileage mag niet negatief zijn, begint op 0
# • panel is een boolean die representeert of het scherm kapot is of niet
# • batterypack is het accupakket, lees verderop wat hierin moet zitten, sommige
# dingen kan je pas compleet maken als je het accupakket gemaakt hebt.
from tesla.Battery import Battery
from random import randint


class Tesla:
    types = ('S', 'X', '3', 'Y')
    colors = ("Deep Blue", "Midnight Silver", "Pearl White", "Red", "Solid Black")
    type = ''
    color = ""
    mileage = 0
    broken_panel = False
    panel_might_break = 0
    Battery

    def __init__(self, tesla_type, tesla_color):
        self.type = tesla_type
        self.color = tesla_color
        temp = randint(0.001, 100)
        if temp < 0.001 * len(self.color):
            self.broken_panel = True

    def drive(self, distance):
        if distance >= 42:
            temp = randint(0, 100)
            if temp <= 5:
                self.broken_panel = True

        if self.broken_panel is True:
            self.mileage += distance
            Battery.juice((ord(type) / 100) * distance)

    def needs_charge(self):
        if self.Battery.status < 20:
            return True
        else:
            return False

    def can_drive(self):
        if not self.broken_panel and not Battery.broken and Battery.status > 0:
            return True
        return False

    def range(self):
        mile = 0
        while True:
            if (ord(type) / 100) * mile == 100:
                return mile
            mile += 1

    def __str__(self):
        return "I am a Tesla model " + self.type + " I have driven " + self.mileage + " my color is " + self.color + " panel is broken: " + self.broken_panel + "."

# Bouw de klasse Tesla in Python die in elk geval de volgende eigenschappen bezit:
# • type kan de waarde S, X, 3 of Y hebben
# • color kan de waarde Deep Blue, Midnight Silver, Pearl White, Red, Solid
# Black
# • mileage mag niet negatief zijn, begint op 0
# • panel is een boolean die representeert of het scherm kapot is of niet
# • batterypack is het accupakket, lees verderop wat hierin moet zitten, sommige
# dingen kan je pas compleet maken als je het accupakket gemaakt hebt.


class Tesla:
    types = ('S', 'X', '3', 'Y')
    colors = ("Deep Blue", "Midnight Silver", "Pearl White", "Red", "Solid Black")
    type = ''
    color = ""
    mileage = 0
    panel = False

    def __init__(self, type, color):
        self.type = type
        self.color = color

from boederij.Animal import Animal


class Alpaca(Animal):
    def __init__(self, name, color="Purple"):
        super(Alpaca, self).__init__(color, name, "Alpaca")


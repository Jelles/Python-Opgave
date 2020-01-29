from boederij.Animal import Animal


class Llama(Animal):
    def __init__(self, name, color="Purple"):
        super(Llama, self).__init__(color, name, "Llama")

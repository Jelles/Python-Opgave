class Animal:
    nickname = ""
    name = ""
    age = 0
    color = "black"
    limit_color = "gray"
    limit_age = 8

    def __init__(self, color, animal_nickname, animal_name):
        self.color = color
        self.nickname = animal_nickname
        self.name = animal_name

    def revive(self):
        if self.age > 0:
            self.age -= 1

    def birthday(self):
        self.age += 1
        print("Yiehaa, birthday " + self.name + "!")
        if self.age >= self.limit_age:
            self.color = self.limit_color
            print("Oh no, my hairs are turning grey!")

    def age_fast(self, years):
        for _ in range(0, years, 1):
            self.birthday()

    def __str__(self):
        return "I am " + self.nickname + " the " + self.color + " " + self.name + " and I am " + str(self.age) + " years old"

from random import randint


class Battery:
    kwhs = (70, 85, 100)
    kwh = 0
    status = 0
    n_charged = 0
    broken = False

    def __init__(self, kwh):
        self.check_kwh(kwh)

    def charge(self):
        if self.n_charged >= 10000:
            self.broken = True
        if self.status is not 100 and not self.broken:
            self.status += randint(20, self.kwh)
            self.n_charged += 1
        if self.status > 100:
            self.status = 100

    def __check_kwh__(self, kwh):
        if kwh not in self.kwhs:
            self.kwh = 70
        self.kwh = kwh

    def juice(self, kwh):
        self.status -= kwh
        if self.status <= 0:
            self.broken = True

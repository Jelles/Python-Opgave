modules = (
    123, 124515, 555, 1, 5, 16, 45, 78, 94, 894894, 8948, 5, 645612, 8465, 56456, 12, 15456, 4568, 48, 456456, 4566, 9,
    4949794856, 2323, 15456, 231865, 891, 564, 41, 7897, 4)


def brandstof(lijst):
    totaal = 0
    for x in lijst:
        totaal += x // 3 - 2
    return totaal


if __name__ == '__main__':
    assert brandstof(modules) == 1650758205

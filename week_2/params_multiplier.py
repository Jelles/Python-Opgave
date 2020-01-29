def multiple(*argv, multiplier):
    total = 0
    for x in argv:
        total += x * multiplier
    return total


if __name__ == '__main__':
    multiple(3, 4, 5, 6, multiplier=3)

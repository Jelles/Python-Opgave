def multiple(elements, multiplier):
    total = 0
    for x in elements:
        total += x * multiplier
    return total


def main():
    numbers = (1, 2)
    print(int(multiple(numbers, 2)))


main()

assert (multiple([3, 4, 99, 1, 4], 31) == 3441)
assert (multiple((3, 1, 3), -12) == -84)
assert (multiple((9, 3215, 31, 6, 5, 4, 23, 52, 35, 26, 6, 26, 46, 4, 8, 42, 2, 77, 685, 24, 24), 102) == 443700)

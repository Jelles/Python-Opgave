woorden = ["Hoi", "ik", "ben", "cool"]


def count_char(input):
    return [len(i) for i in input]


if __name__ == '__main__':
    print(count_char(woorden))

import math


def grootste_gemene_deler(a, b):
    return math.gcd(a, b)


if __name__ == '__main__':
    assert(grootste_gemene_deler(5, 10) == 5)  # 5
    assert(grootste_gemene_deler(44, 12) == 4) # 4
    print(grootste_gemene_deler(23, 69) == 23)  # 5 ?? 23
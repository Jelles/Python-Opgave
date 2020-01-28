def count_char(line):
    upper = 0
    lower = 0
    for x in line:
        if x.islower():
            lower += 1
        if x.isupper():
            upper += 1
    return upper, lower


if __name__ == '__main__':
    uppers, lowers = count_char("Do not try and bend the spoon, that's impossible. \
    Instead, only try to realize the truth... there is no spoon. ")
    assert (uppers == 2 and lowers == 81)

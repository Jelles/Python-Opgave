def whitespace_count(input):
    return len([i for i in input if (i == ' ')])


if __name__ == '__main__':
    print(whitespace_count("    a    a    a    "))


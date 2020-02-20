articles = {"television": 699, "subwoofer": 249.99, "beamer": 2325, "soundbar": 299, "IP cam": 124.95}


def format_(items):
    for x in items:
        print(str.ljust(x, 15), '$', str.rjust(str(items[x]), 10))


if __name__ == '__main__':
    format_(articles)
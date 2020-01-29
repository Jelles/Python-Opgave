def unicount(word):
    result = 0
    for c in word:
        result += ord(c)
    return result


def unimaster(func, words):
    result = 0
    for word in words:
        result += func(word)
    return result


if __name__ == "__main__":
    story = "If you don’t know who I am, then maybe your best \
     course would be to tread lightly.".split()
    print(unimaster(unicount, story)) # should print 15109!`q   
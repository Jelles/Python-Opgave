def weird_numbers(min_range=1500, max_range=3297):
    return_value = []
    for x in range(min_range, max_range, 1):
        if x % 7 == 0 and not x % 5 == 0:
            return_value.append(x)
    return return_value


if __name__ == '__main__':
    print(*weird_numbers(), sep=',')
    print(*weird_numbers(max_range=3500), sep=',')

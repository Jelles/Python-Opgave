def only_even(numbers):
    return_value = []
    for x in numbers:
        if x % 2 == 0:
            return_value.append(x)
    return return_value


def main():
    numbers = [5, 15, 12, 2, 353, 1, 5151]
    answer = only_even(numbers)
    print(answer)


main()

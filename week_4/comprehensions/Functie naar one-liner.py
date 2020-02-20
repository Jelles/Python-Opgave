numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def delete_even(numbers):
    new_list = []
    for i in numbers:
        if i % 2 != 0:
            new_list.append(i)
    return new_list


def delete_even_comprehension(numbers):
    return [i for i in numbers if (i % 2 != 0)]


if __name__ == '__main__':
    # print(delete_even(numbers))
    print(delete_even_comprehension(numbers))

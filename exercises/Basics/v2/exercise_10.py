def to_binary_match(number: int) -> list[bool]:
    number %= 8
    match number:
        case 0:
            return [False, False, False]
        case 1:
            return [False, False, True]
        case 2:
            return [False, True, False]
        case 3:
            return [False, True, True]
        case 4:
            return [True, False, False]
        case 5:
            return [True, False, True]
        case 6:
            return [True, True, False]
        case 7:
            return [True, True, True]


def to_binary_dict(number: int) -> list[bool]:
    dictionary = {0: [False, False, False], 1: [False, False, True], 2: [False, True, False], 3: [False, True, True],
                  4: [True, False, False],
                  5: [True, False, True], 6: [True, True, False], 7: [True, True, True]}
    number %= 8
    return dictionary[number]


if __name__ == '__main__':
    print(to_binary_match(3))
    print(to_binary_match(8))
    print(to_binary_dict(3))
    print(to_binary_dict(8))
    pass

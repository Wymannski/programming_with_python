def to_binary(number: int) -> list[bool]:
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
        case _:
            raise Exception("Number must be smaller than 8")


def to_binary_dictionary(number: int) -> list[bool]:
    dictionary = {
        0:
            [False, False, False],
        1:
            [False, False, True],
        2:
            [False, True, False],
        3:
            [False, True, True],
        4:
            [True, False, False],
        5:
            [True, False, True],
        6:
            [True, True, False],
        7:
            [True, True, True]
    }
    if number < 8:
        return dictionary[number]
    else:
        raise Exception("Number must be smaller than 8")


print(to_binary(1))
print(to_binary_dictionary(1))

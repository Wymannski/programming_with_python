from functools import reduce
from typing import Any


def all_same_length(lla: list[list[Any]]) -> bool:
    if not lla:
        return True
    length = list(map(len,lla))
    test = map(lambda x: x== len(lla[0]),length)
    return reduce(lambda a,b: a and b,test)

def main():
    lst_1 = [[1,2],[3,4],[5,6]]
    lst_2 = [[1,2],[3,4],[5]]

    print(all_same_length(lst_1))
    print(all_same_length(lst_2))


if __name__ == '__main__':
    main()
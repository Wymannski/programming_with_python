from functools import reduce
from typing import Any


def all_same_length(lla: list[list[Any]]) -> bool:
    if not lla:
        return True
    length = list(map(len,lla))
    test = map(lambda x: x== len(lla[0]),length)
    return reduce(lambda a,b: a and b,test)

def sum_same_index(llf: list[list[float]]) -> list[float]:
    if not all_same_length(llf):
        raise NotSameLengthException()
    if not llf or len(llf[0]) < 1:
        return []
    lst = map(lambda x: x[0],llf)
    return [reduce(lambda a,b: a+b,lst)] + sum_same_index(list(map(lambda a: a[1:],llf)))

class NotSameLengthException(Exception):
    def __init__(self,message = "Not all sublist have the same length"):
        super().__init__(message)


def main():
    lst = [[1.0,2.0,3.0,4.0], [1.0,2.0,3.0,4.0], [1.0,2.0,3.0,4.0]]
    print(sum_same_index(lst))

if __name__ == '__main__':
    main()
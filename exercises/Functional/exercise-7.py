import operator
from functools import reduce


def product(items:list[int])->int:
    return reduce(operator.mul,items)

def main():
    ints = [1,2,3,4]
    print(product(ints))

if __name__ == '__main__':
    main()
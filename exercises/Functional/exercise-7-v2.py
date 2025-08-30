import operator
from functools import reduce


def prod_list(items:list[int])->int:
    return reduce(operator.mul,items)


def main():
    items = [1,2,3,4]
    print(prod_list(items))


if __name__ == '__main__':
    main()
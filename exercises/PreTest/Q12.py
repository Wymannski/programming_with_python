from itertools import count
from math import sqrt

from pycparser.ply.yacc import resultlimit


def read_universe() -> list[list[int]]:
    try:
        with open('alien.txt', 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('File not found')

    lst = []
    if lines:
        for line in lines:
            values = line.split()
            line_val = []
            for value in values:
                if value == 'X':
                    line_val.append(100)
                elif value == 'Y':
                    line_val.append(101)
                else:
                    line_val.append(int(value))
            lst.append(line_val)
            line_val = []

    return lst


def common_divisor(a: int, b: int) -> bool:
    n = gcd(a, b)

    result = 0
    for i in range(1, int(sqrt(n)) + 1):

        if n % i == 0:

            if n / i == i:
                result += 1
            else:
                result += 2

    return result > 1


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def find_path(matrix:list[list[int]]) -> list[int]:
    result = []
    findPathRec(result,matrix,0, 0)
    return result



def findPathRec(result, matrix, i: int, j: int) -> bool:
    if not is_inside(matrix,i,j):
        return False
    if matrix[i][j] == 101:
        return True

    if is_valid_move(matrix, matrix[i][j], i, j):
        if findPathRec(result,matrix, i - 1, j):
            result.append(matrix[i-1][j])
            return True
        if findPathRec(result, matrix, i + 1, j):
            result.append(matrix[i+1][j])
            return True
        if findPathRec(result,matrix, i, j - 1):
            result.append(matrix[i][j-1])
            return True
        if findPathRec(result, matrix, i, j + 1):
            result.append(matrix[i][j+1])
            return True
        return False
    return False

def is_valid_move(matrix, prev: int, i: int, j: int) -> bool:
    return is_inside(matrix, i, j) and (common_divisor(prev, matrix[i][j]))


def is_inside(matrix, i, j):
    return i < len(matrix) and j < len(matrix[0])



def main():
    lst = read_universe()
    print(lst)

    result = []

    print(common_divisor(6, 3))
    print(common_divisor(5, 2))

    find_path(lst)


if __name__ == '__main__':
    main()

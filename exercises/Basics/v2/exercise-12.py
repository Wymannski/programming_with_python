def transpose(items:list[list])->list[list]:
    if not items or not items[0]:
        return []
    return [list(map(lambda a:a[0],items))] + transpose(list(map(lambda b:b[1:],items)))

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(transpose(matrix))
    pass
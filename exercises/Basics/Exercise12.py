def transpose(matrix: list[list]) -> list[list]:
    if len(matrix) != len(matrix[0]):
        raise Exception("The amount of columns is not equal to the amount of rows.")
    result = []
    for index_col in range(len(matrix[0])):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[index_col])
        result.append(transposed_row)
    return result

def transpose_short(matrix: list[list]) -> list[list]:
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(transpose(matrix))
print(transpose_short(matrix))



mat = [[1, 2], [3, 4]]
def transpose(mat: list[list[float | int]]) -> list[list]:
    row = len(mat[0])
    result = []
    if not mat:
        return []
    for i in mat:
        if row != len(i):
            return ValueError
    else:
        result = [list(i) for i in zip(*mat)]
        return result
print(transpose(mat))

mat = [[1,2], [3,4]]
def row_sums(mat: list[list[float | int]]) -> list[float]:
    row_length = len(mat[0])
    result = []
    for row in mat:
        if row_length != len(row):
            return ValueError
        else:
            result.append(sum(row))
    return result
print(row_sums(mat))



def col_sums(mat: list[list[float | int]]) -> list[float]:
    height_column = len(mat[0])
    result = []
    for column in mat:
        if height_column != len(column):
            return ValueError
        else:
            result = [sum(column) for column in zip(*mat)]
            return result
print(col_sums(mat))
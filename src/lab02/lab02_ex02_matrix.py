transpose_mat = [[1, 2, 3]] #сюда тест кейс
def transpose(transpose_mat: list[list[float | int]]) -> list[list]:
    result = []
    if not transpose_mat:
        return []
    for i in transpose_mat:
        if len(transpose_mat[0]) != len(i):
            return ValueError
    else:
        result = [list(i) for i in zip(*transpose_mat)]
        return result
print("transpose", transpose_mat, "--->", transpose(transpose_mat))

row_mat = [[1, 2, 3], [4, 5, 6]] #сюда тест кейс
def row_sums(row_mat: list[list[float | int]]) -> list[float]:
    result = []
    for row in row_mat:
        if len(row_mat[0]) != len(row):
            return ValueError
        else:
            result.append(sum(row))
    return result
print("row_sums", row_mat, "--->", row_sums(row_mat))


col_mat = [[1, 2, 3], [4, 5, 6]] #сюда тест кейс
def col_sums(col_mat: list[list[float | int]]) -> list[float]:
    result = []
    for row in row_mat:
        if len(row_mat[0]) != len(row):
                return ValueError
        else:
            result = [sum(col) for col in zip(*col_mat)]
    return result
print("col_sums", col_mat, "--->", col_sums(col_mat))
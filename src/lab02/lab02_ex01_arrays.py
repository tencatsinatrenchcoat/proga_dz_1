nums_minmax = [1.5, 2, 2.0, -3.1]  # сюда тест кейс


def min_max(nums_minmax: list[float | int]) -> tuple[float | int, float | int]:
    if not nums_minmax:
        return ValueError
    if nums_minmax:
        small_num = nums_minmax[0]
        big_num = nums_minmax[0]
        for i in nums_minmax:
            if i < small_num:
                small_num = i
            if i > big_num:
                big_num = i
    return small_num, big_num


print("min_max", nums_minmax, "--->", min_max(nums_minmax))

nums_unique = [1.0, 1, 2.5, 2.5, 0]  # cюда тест кейс


def unique_sorted(nums_unique: list[float | int]) -> list[float | int]:
    if not nums_unique:
        return TypeError
    else:
        result = set(nums_unique)
        result = sorted(result)
        return result


print("unique_sorted", nums_unique, "--->", unique_sorted(nums_unique))


mat = [[1, 2], (3, 4, 5)]  # cюда тест кейс


def flatten(mat: list[list | tuple]) -> list:
    result = []
    for rows in mat:
        if not isinstance(rows, (list, tuple)):
            return TypeError
        for i in rows:
            result.append(i)
    return result


print("flatten", mat, "--->", flatten(mat))

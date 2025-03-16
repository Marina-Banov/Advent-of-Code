def visible_in_direction(matrix, i, j, dirs, row_range, col_range):
    n = 0
    for k in row_range:
        for l in col_range:
            if (k, l) == (i, j):
                continue
            diff_y = k - i
            diff_x = l - j
            if (diff_y, diff_x) in dirs:
                continue
            found = False
            while i + diff_y >= 0 and j + diff_x >= 0:
                try:
                    if matrix[i + diff_y][j + diff_x] == '#' and not found:
                        n += 1
                        found = True
                    dirs.add((diff_y, diff_x))
                    while (diff_y, diff_x) in dirs:
                        diff_x += l - j
                        diff_y += k - i
                except Exception as _:
                    break
    return n


def part_one(matrix):
    keep_score = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '.':
                continue
            dirs = set()
            n = visible_in_direction(matrix, i, j, dirs, range(i, -1, -1), range(j, -1, -1))
            n += visible_in_direction(matrix, i, j, dirs, range(i, -1, -1), range(j, len(matrix[0])))
            n += visible_in_direction(matrix, i, j, dirs, range(i, len(matrix)), range(j, -1, -1))
            n += visible_in_direction(matrix, i, j, dirs, range(i, len(matrix)), range(j, len(matrix[0])))
            keep_score = max(keep_score, n)
    return keep_score


def part_two(_):
    return


def main(fn):
    with open("input", "r") as f:
        matrix = [list(line.strip()) for line in f.readlines()]
    return fn(matrix)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

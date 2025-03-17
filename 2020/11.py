from itertools import chain, product, starmap


def part_one(matrix, i, j):
    return list(starmap(lambda a, b: matrix[i + a][j + b], product((0, -1, +1), (0, -1, +1))))


def part_two(matrix, i, j):
    # returns the first adjacent seat in all directions
    rules = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    adjacent = []
    for rule in rules:
        a = i + rule[0]
        b = j + rule[1]
        while matrix[a][b] is None and 0 < a < len(matrix)-1 and 0 < b < len(matrix[0])-1:
            a += rule[0]
            b += rule[1]
        if matrix[a][b] is not None:
            adjacent.append(matrix[a][b])
    return adjacent


def simulate(matrix, fn):
    flag = True
    while flag:
        flag = False
        changed = []
        for i in range(1, len(matrix) - 1):
            for j in range(1, len(matrix[0]) - 1):
                if matrix[i][j] is None:
                    continue
                adjacent = fn(matrix, i, j)
                occupied = adjacent.count(True)
                if (not matrix[i][j] and occupied == 0) or (matrix[i][j] and occupied >= 5):
                    # larger than 5 because list adjacent contains matrix[i][j] as well
                    changed.append([i, j])
                    flag = True
        # only access seats which changed their occupied status
        for a, b in changed:
            matrix[a][b] = not matrix[a][b]
    return len([seat for seat in chain.from_iterable(matrix) if seat])


def get_matrix(lines):
    # would prefer to work with boolean values rather than strings
    # legend: - floor ('.')    --> None
    #         - occupied ('#') --> True
    #         - free ('L')     --> False
    # adding floor around the given grid to avoid border checking
    n_rows, n_cols = len(lines) + 2, len(lines[0]) + 2
    matrix = [[None for _ in range(n_cols)] for _ in range(n_rows)]
    for i in range(1, n_rows - 1):
        for j in range(1, n_cols - 1):
            if lines[i - 1][j - 1] != '.':
                matrix[i][j] = False
    return matrix


def main(fn):
    with open("input", "r") as f:
        lines = f.read().strip().split()
    matrix = get_matrix(lines)
    del lines
    return simulate(matrix, fn)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

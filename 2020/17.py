from itertools import chain, product, starmap


def simulate(matrix, rules, w_range):
    nx, ny = len(matrix[0][0][0]), len(matrix[0][0])
    active_cubes = list(chain.from_iterable(matrix[8][8][7:ny - 7])).count(True)
    for i in range(6):
        changed = []
        for w in w_range(i):
            for z in range(7 - i, 10 + i):
                for y in range(6 - i, ny - 6 + i):
                    for x in range(6 - i, nx - 6 + i):
                        active_adj = [matrix[w + r[0]][z + r[1]][y + r[2]][x + r[3]] for r in rules].count(True)
                        if matrix[w][z][y][x] and active_adj not in [2, 3] or not matrix[w][z][y][x] and active_adj == 3:
                            changed.append((x, y, z, w))
        for x, y, z, w in changed:
            matrix[w][z][y][x] = not matrix[w][z][y][x]
            if matrix[w][z][y][x]:
                active_cubes += 1
            else:
                active_cubes -= 1
    return active_cubes


def part_one():
    rules = list(set(starmap(lambda a, b, c, d: (a, b, c, d), product((0, 0, 0), (0, -1, +1), (0, -1, +1), (0, -1, +1)))))
    rules.remove((0, 0, 0, 0))
    return rules, lambda i: [8]


def part_two():
    rules = list(starmap(lambda a, b, c, d: (a, b, c, d), product((0, -1, +1), (0, -1, +1), (0, -1, +1), (0, -1, +1))))
    rules.remove((0, 0, 0, 0))
    return rules, lambda i: range(7 - i, 10 + i)


def get_matrix(lines):
    # similarly to day 11, would prefer to work with boolean values rather than strings
    # creating a new, larger matrix
    # the idea is to add inactive cubes around the given grid to avoid border checking
    # legend: - inactive ('.') --> False
    #         - active ('#')   --> True
    nx, ny = len(lines[0]) + 14, len(lines) + 14
    matrix = [[[[False for _ in range(nx)] for _ in range(ny)] for _ in range(3 + 14)] for _ in range(3 + 14)]
    for i in range(7, ny - 7):
        for j in range(7, nx - 7):
            matrix[8][8][i][j] = (lines[i - 7][j - 7] == '#')
    return matrix


def main(fn):
    with open("input", "r") as f:
        lines = f.read().strip().split()
    matrix = get_matrix(lines)
    del lines
    rules, w_range = fn()
    return simulate(matrix, rules, w_range)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

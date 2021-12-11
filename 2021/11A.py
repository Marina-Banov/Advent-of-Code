def get_adjacent(i, j):
    DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return [(i+d[0], j+d[1]) for d in DIRECTIONS if 0 <= i+d[0] < 10 and 0 <= j+d[1] < 10]


def get_flash_indices():
    return [(i, j) for i, row in enumerate(matrix) for j, val in enumerate(row) if val >= 10]


def increase_energy():
    return [[octopus+1 for octopus in row] for row in matrix]


f = open("input.txt", "r")

matrix = [list(map(int, line.strip())) for line in f]
adjacent = [get_adjacent(i, j) for i in range(10) for j in range(10)]
res = 0

for step in range(100):
    matrix = increase_energy()
    flashes = get_flash_indices()
    while len(flashes) > 0:
        for (i, j) in flashes:
            matrix[i][j] = 0
            for (a_i, a_j) in adjacent[i*10 + j]:
                if matrix[a_i][a_j] != 0:
                    matrix[a_i][a_j] += 1
        res += len(flashes)
        flashes = get_flash_indices()

print(res)

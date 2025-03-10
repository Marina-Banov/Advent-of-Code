from itertools import chain, product, starmap


def should_skip(w, z, i):
    if z == 8:
        return False
    it = 1 if z < 8 else -1
    count = list(chain.from_iterable(matrix[w][z+it][7-i-1:ny-7+1+i])).count(True)
    return count == 0


f = open("input.txt", 'r').read().strip().split()
nx, ny = len(f[0]) + 14, len(f) + 14
matrix = [[[[False for x in range(nx)] for y in range(ny)] for z in range(3 + 14)] for w in range(3 + 14)]
for i in range(7, ny-7):
    for j in range(7, nx-7):
        matrix[8][8][i][j] = (f[i-7][j-7] == '#')

active_cubes = list(chain.from_iterable(matrix[8][8][7:ny-7])).count(True)
rules = list(starmap(lambda a, b, c, d: [a, b, c, d], product((0, -1, +1), (0, -1, +1), (0, -1, +1), (0, -1, +1))))
rules.remove([0, 0, 0, 0])

for i in range(6):
    changed = []
    for w in range(7-i, 10+i):
        for z in range(7-i, 10+i):
            for y in range(6-i, ny-6+i):
                for x in range(6-i, nx-6+i):
                    active_adj = [matrix[w + r[0]][z + r[1]][y + r[2]][x + r[3]] for r in rules].count(True)
                    if matrix[w][z][y][x] and active_adj not in [2, 3] or not matrix[w][z][y][x] and active_adj == 3:
                        changed.append((x, y, z, w))

    for x, y, z, w in changed:
        matrix[w][z][y][x] = not matrix[w][z][y][x]
        if matrix[w][z][y][x]:
            active_cubes += 1
        else:
            active_cubes -= 1

print(active_cubes)

from itertools import chain, product, starmap


def should_skip(z, i):
    if z == 8:
        return False
    it = 1 if z < 8 else -1
    count = list(chain.from_iterable(matrix[z+it][7-i-1:ny-7+1+i])).count(True)
    return count == 0


f = open("input.txt", 'r').read().strip().split()

# similarly to day 11, would prefer to work with boolean values rather than strings
# creating a new, larger matrix
# the idea is to add inactive cubes around the given grid to avoid border checking
# legend: - inactive ('.') --> False
#         - active ('#')   --> True
nx, ny = len(f[0]) + 14, len(f) + 14
matrix = [[[False for x in range(nx)] for y in range(ny)] for z in range(3 + 14)]
for i in range(7, ny-7):
    for j in range(7, nx-7):
        matrix[8][i][j] = (f[i-7][j-7] == '#')

active_cubes = list(chain.from_iterable(matrix[8][7:ny-7])).count(True)
rules = list(starmap(lambda a, b, c: [a, b, c], product((0, -1, +1), (0, -1, +1), (0, -1, +1))))
rules.remove([0, 0, 0])

for i in range(6):
    changed = []
    for z in range(7-i, 10+i):
        if should_skip(z, i):
            continue

        for y in range(6-i, ny-6+i):
            for x in range(6-i, nx-6+i):
                active_adj = [matrix[z + rule[0]][y + rule[1]][x + rule[2]] for rule in rules].count(True)
                if matrix[z][y][x] and active_adj not in [2, 3] or not matrix[z][y][x] and active_adj == 3:
                    changed.append((x, y, z))

    for x, y, z in changed:
        matrix[z][y][x] = not matrix[z][y][x]
        if matrix[z][y][x]:
            active_cubes += 1
        else:
            active_cubes -= 1

print(active_cubes)

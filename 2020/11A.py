from itertools import chain, product, starmap


f = open("input.txt", "r").read().strip().split()

# would prefer to work with boolean values rather than strings
# creating a new, larger matrix
# the idea is to add floor around the given grid to avoid border checking
# legend: - floor ('.')    --> None
#         - occupied ('#') --> True
#         - free ('L')     --> False
rows, cols = len(f) + 2, len(f[0]) + 2
matrix = [[None for x in range(cols)] for y in range(rows)]
for i in range(1, rows-1):
    for j in range(1, cols-1):
        if f[i-1][j-1] != '.':
            matrix[i][j] = (f[i-1][j-1] == '#')
del f  # no longer needed

flag = True
while flag:
    flag = False
    changed = []

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if matrix[i][j] is None:
                continue

            adjacent = list(starmap(lambda a, b: matrix[i+a][j+b], product((0, -1, +1), (0, -1, +1))))
            occupied = adjacent.count(True)
            if (not matrix[i][j] and occupied == 0) or (matrix[i][j] and occupied >= 5):
                # larger than 5 because list adjacent contains matrix[i][j] as well
                changed.append([i, j])
                flag = True

    # only access seats which changed their occupied status
    for a, b in changed:
        matrix[a][b] = not matrix[a][b]

print(len([seat for seat in chain.from_iterable(matrix) if seat]))

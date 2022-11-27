from itertools import chain


# returns the coordinates of the first adjacent seat in all directions
def get_adjacent_seats(i, j):
    rules = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    adjacent = []
    for rule in rules:
        a = i + rule[0]
        b = j + rule[1]
        while f[a][b] == '.' and a > 0 and b > 0 and a < rows-1 and b < cols-1:
            a += rule[0]
            b += rule[1]
        if f[a][b] != '.':
            adjacent.append([a, b])
    return adjacent


# adding floor around the given grid to avoid border checking
f = open("input.txt", 'r').read().strip().split()
rows, cols = len(f) + 2, len(f[0]) + 2
f.insert(0, '.' * cols)
for i in range(1, rows-1):
    f[i] = "".join(('.', f[i], '.'))
f.append('.' * cols)

# would prefer to work with boolean values rather than strings
# storing the occupied status and array of adjacent seats for each cell
# floor is not relevant for the computation so those cells can remain None
matrix = [[None for x in range(cols)] for y in range(rows)]
for i in range(1, rows-1):
    for j in range(1, cols-1):
        if f[i][j] != '.':
            matrix[i][j] = {
                "occupied": (f[i][j] == '#'),
                "adjacent": get_adjacent_seats(i, j)
            }
del f  # no longer needed

flag = True
while flag:
    flag = False
    changed = []

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if matrix[i][j] is None:
                continue

            occupied = 0
            for a, b in matrix[i][j]["adjacent"]:
                if matrix[a][b]["occupied"]:
                    occupied += 1
            if (not matrix[i][j]["occupied"] and occupied == 0) or (matrix[i][j]["occupied"] and occupied >= 5):
                changed.append([i, j])
                flag = True

    # only access seats which changed their occupied status
    for a, b in changed:
        matrix[a][b]["occupied"] = not matrix[a][b]["occupied"]

print(len([seat for seat in chain.from_iterable(matrix) if seat and seat["occupied"]]))

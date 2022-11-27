def dfs(i, j, basin_size):
    basin_size += 1
    lines[i][j] = -1

    neighbours = []
    if i > 0:
        neighbours.append((i-1, j))
    if i < rows-1:
        neighbours.append((i+1, j))
    if j > 0:
        neighbours.append((i, j-1))
    if j < cols-1:
        neighbours.append((i, j+1))

    for n_i, n_j in neighbours:
        if -1 < lines[n_i][n_j] < 9:
            basin_size = dfs(n_i, n_j, basin_size)

    return basin_size


f = open("input.txt", 'r')

lines = [list(map(int, list(line.strip()))) for line in f.readlines()]
rows, cols = len(lines), len(lines[0])
basins = []

for i in range(rows):
    for j in range(cols):
        if -1 < lines[i][j] < 9:
            basins.append(dfs(i, j, 0))

basins.sort()

print(basins[-1] * basins[-2] * basins[-3])

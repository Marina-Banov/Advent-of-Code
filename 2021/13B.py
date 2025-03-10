f = open("input.txt", 'r')

matrix = [[' ']]

while True:
    line = f.readline().strip()
    if line == "":
        break
    x, y = list(map(int, line.split(',')))

    n_row, n_col = len(matrix), len(matrix[0])
    new_n_row = max(y+1, n_row)
    new_n_col = max(x+1, n_col)

    if x >= n_col or y >= n_row:
        matrix = [[matrix[i][j] if j < n_col and i < n_row else ' ' for j in range(new_n_col)] for i in range(new_n_row)]

    matrix[y][x] = '#'

while True:
    line = f.readline().strip()
    if line == "":
        break
    val = int(line.split('=')[1])
    n_row, n_col = len(matrix), len(matrix[0])

    if line[11] == 'x':
        new_n_row = n_row
        new_n_col = val
        start_row = 0
        start_col = val + 1
        row_fun = lambda i : i
        col_fun = lambda j : 2 * val - j
    else:
        new_n_row = val
        new_n_col = n_col
        start_row = val + 1
        start_col = 0
        row_fun = lambda i : 2 * val - i
        col_fun = lambda j : j

    new_matrix = [[matrix[i][j] for j in range(new_n_col)] for i in range(new_n_row)]

    for i in range(start_row, n_row):
        for j in range(start_col, n_col):
            if matrix[i][j] == '#':
                new_matrix[row_fun(i)][col_fun(j)] = '#'

    matrix = new_matrix

for row in matrix:
    print("".join(row))

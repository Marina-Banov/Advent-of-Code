f = open("input.txt", 'r')

matrix = [['.']]

while True:
    line = f.readline().strip()
    if line == "":
        break
    x, y = list(map(int, line.split(',')))

    n_col = len(matrix[0])
    n_row = len(matrix)
    if x >= n_col:
        matrix = [[matrix[i][j] if j < n_col else '.' for j in range(x+1)] for i in range(n_row)]
    
    n_col = len(matrix[0])
    if y >= n_row:
        matrix = [[matrix[i][j] if i < n_row else '.' for j in range(n_col)] for i in range(y+1)]

    matrix[y][x] = '#'

axis = f.readline()[11]

if axis == 'x':
    matrix = [[matrix[i][j] if matrix[i][j] == '#' else matrix[i][n_col-1-j] for j in range(int(n_col/2))] for i in range(n_row)]
else:
    matrix = [[matrix[i][j] if matrix[i][j] == '#' else matrix[n_row-1-i][j] for j in range(n_col)] for i in range(int(n_row/2))]

print(sum([True if el == '#' else False for row in matrix for el in row]))

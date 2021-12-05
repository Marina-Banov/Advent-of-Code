import re


matrix = [[0 for j in range(1000)] for i in range(1000)]

with open("input.txt", "r") as f:
    for line in f.readlines():
        x1, y1, x2, y2 = list(map(int, re.split(",| -> ", line.strip())))
        xs = list(range(min(x1, x2), max(x1+1, x2+1)))
        ys = list(range(min(y1, y2), max(y1+1, y2+1)))

        if x1 == x2:
            for i in ys:
                matrix[i][x1] += 1
        elif y1 == y2:
            for j in xs:
                matrix[y1][j] += 1

print(sum([el >= 2 for row in matrix for el in row]))

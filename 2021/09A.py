f = open("input.txt", "r").readlines()

res = 0

for i in range(len(f)):
    row = list(map(int, list(f[i].strip())))

    for j, val in enumerate(row):
        if val == 9:
            continue

        if i > 0 and val >= int(f[i-1][j]):
            continue

        if i < len(f)-1 and val >= int(f[i+1][j]):
            continue

        if j > 0 and val >= row[j-1]:
            continue

        if j < len(row)-1 and val >= row[j+1]:
            continue

        res += val + 1

print(res)

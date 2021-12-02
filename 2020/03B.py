def check_for_tree(path, i):
    if x[i] >= len(path):
        x[i] %= len(path)
    if path[x[i]] == '#':
        return 1
    return 0


f = open("input.txt", "r")
trees = [0, 0, 0, 0, 0]
x = [0, 0, 0, 0, 0]
y = True

while True:
    path = f.readline().strip()
    if path == '':
        break

    for i in range(4):
        trees[i] += check_for_tree(path, i)

    if y:
        trees[4] += check_for_tree(path, 4)
        x[4] += 1

    x[0] += 1
    x[1] += 3
    x[2] += 5
    x[3] += 7
    y = not y

res = 1
for i in range(5):
    res *= trees[i]
print(res)

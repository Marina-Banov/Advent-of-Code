f = open("input.txt", "r")
trees = 0
x = 0

while True:
    path = f.readline().strip()
    if path == '':
        break
    if x >= len(path):
        x %= len(path)
    if path[x] == '#':
        trees += 1
    x += 3

print(trees)

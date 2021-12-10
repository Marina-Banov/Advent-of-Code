f = open("input.txt", "r")

res = []
chunk_start = '([{<'
chunk_end = ')]}>'
for line in f:
    stack = []
    line = line.strip()
    corrupt = False
    for c in line:
        try:
            index_end = chunk_end.index(c)
            m = stack.pop()
            index_start = chunk_start.index(m)
            if index_start != index_end:
                corrupt = True
                break
        except ValueError as e:
            stack.append(c)
    if not corrupt:
        points = 0
        while len(stack) > 0:
            m = stack.pop()
            index_start = chunk_start.index(m)
            points *= 5
            points += index_start + 1
        res.append(points)
res.sort()
print(res[int(len(res) / 2)])

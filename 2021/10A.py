f = open("input.txt", 'r')

res = 0
chunk_start = "([{<"
chunk_end = ")]}>"
error_values = [3, 57, 1197, 25137]
for line in f:
    stack = []
    line = line.strip()
    for c in line:
        try:
            index_end = chunk_end.index(c)
            m = stack.pop()
            index_start = chunk_start.index(m)
            if index_start != index_end:
                res += error_values[index_end]
                break
        except ValueError as e:
            stack.append(c)
print(res)

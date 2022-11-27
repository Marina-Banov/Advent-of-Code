lines = open("input.txt", 'r').read().strip().split("\n")
lines.append("")
all_sum = 0
group = []
for i in range(len(lines)):
    if lines[i] == "":
        all_sum += len(group)
        group = []
        continue
    for j in range(len(lines[i])):
        if not lines[i][j] in group:
            group.append(lines[i][j])
print(all_sum)

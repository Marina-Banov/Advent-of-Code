lines = open("input.txt", "r").read().strip().split('\n')
lines.append('')
all_sum = 0
group = []
singles = []
for i in range(len(lines)):
    if lines[i] == '':
        n_passengers = len(group)
        group = sum(group, [])
        for s in singles:
            if group.count(s) == n_passengers:
                all_sum += 1
        group = []
        singles = []
        continue
    for j in range(len(lines[i])):
        if not lines[i][j] in singles:
            singles.append(lines[i][j])
    group.append([char for char in lines[i]])
print(all_sum)

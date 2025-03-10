def calc_n_paths(i):
    if paths[i] == 0:
        for j in came_from[i]:
            paths[i] += calc_n_paths(j)
    return paths[i]


charges = list(map(int, open("input.txt", 'r').read().strip().split()))
charges.append(0)
charges = sorted(charges)
charges.append(charges[-1] + 3)

came_from = [[] for c in range(len(charges))]
paths = [0 for c in range(len(charges))]
paths[0] = 1

for i in range(len(charges)-1, -1, -1):
    for j in range(i-3, i):
        if j >= 0 and charges[i] - charges[j] <= 3:
            came_from[i].append(j)

print(calc_n_paths(len(charges)-1))

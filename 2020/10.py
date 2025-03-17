def calc_n_paths(paths, came_from, i):
    if paths[i] == 0:
        for j in came_from[i]:
            paths[i] += calc_n_paths(paths, came_from, j)
    return paths[i]


def part_one(charges):
    ones = 0
    threes = 1
    for i in range(len(charges)):
        try:
            if charges[i] + 1 == charges[i + 1]:
                ones += 1
            elif charges[i] + 3 == charges[i + 1]:
                threes += 1
        except Exception as _:
            return ones * threes


def part_two(charges):
    charges.append(charges[-1] + 3)
    came_from = [[] for _ in range(len(charges))]
    paths = [0 for _ in range(len(charges))]
    paths[0] = 1
    for i in range(len(charges)-1, -1, -1):
        for j in range(i-3, i):
            if j >= 0 and charges[i] - charges[j] <= 3:
                came_from[i].append(j)
    return calc_n_paths(paths, came_from, len(charges)-1)


def main(fn):
    with open("input", "r") as f:
        charges = list(map(int, f.read().strip().split()))
    charges.append(0)
    charges = sorted(charges)
    return fn(charges)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

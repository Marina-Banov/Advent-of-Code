def check_for_tree(x, path, i):
    if x[i] >= len(path):
        x[i] %= len(path)
    return path[x[i]] == '#'


def part_one(_map):
    trees = [0]
    x = [0]
    for path in _map:
        if check_for_tree(x, path, 0):
            trees[0] += 1
        x[0] += 3
    return trees[0]


def part_two(_map):
    trees = [0, 0, 0, 0, 0]
    x = [0, 0, 0, 0, 0]
    y = True
    for path in _map:
        for i in range(4):
            trees[i] += check_for_tree(x, path, i)
        if y:
            trees[4] += check_for_tree(x, path, 4)
            x[4] += 1
        x[0] += 1
        x[1] += 3
        x[2] += 5
        x[3] += 7
        y = not y
    res = 1
    for tree in trees:
        res *= tree
    return res


def main(fn):
    _map = []
    with open("input", "r") as f:
        while True:
            path = f.readline().strip()
            if path == "":
                break
            _map.append(path)
    return fn(_map)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

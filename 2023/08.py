from math import lcm


def traverse(cur, stop, _map, steps):
    n = 0
    while not stop(cur):
        cur = _map[cur][steps[n % len(steps)] == "R"]
        n += 1
    return n


def part_one(_map, steps):
    return traverse("AAA", lambda x: x == "ZZZ", _map, steps)


def part_two(_map, steps):
    return lcm(*[
        traverse(key, lambda x: x[2] == "Z", _map, steps)
        for key in _map.keys() if key[2] == "A"
    ])


def main(count_steps):
    with open("input.txt", "r") as f:
        steps = list(f.readline().strip())
        f.readline()
        _map = {}
        for line in f.readlines():
            name, lr = line.strip().split(" = ")
            _map[name] = lr[1:-1].split(", ")
    return count_steps(_map, steps)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

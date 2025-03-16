directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}


def run_wire(wire1):
    pos = (0, 0)
    points = set()
    n_steps = 0
    steps_a = {}
    for i in wire1:
        for j in range(1, int(i[1:]) + 1):
            pos = tuple(map(sum, zip(pos, directions[i[0]])))
            n_steps += 1
            points.update([pos])
            steps_a[str(pos)] = n_steps
    return points, steps_a


def part_one(wire1, wire2):
    points, _ = run_wire(wire1)
    min_res = 99999999
    pos = (0, 0)
    for i in wire2:
        for j in range(1, int(i[1:]) + 1):
            pos = tuple(map(sum, zip(pos, directions[i[0]])))
            if pos in points:
                min_res = min(min_res, abs(pos[0]) + abs(pos[1]))
    return min_res


def part_two(wire1, wire2):
    points, steps_a = run_wire(wire1)
    min_res = 99999999
    pos = (0, 0)
    n_steps = 0
    for i in wire2:
        for j in range(1, int(i[1:]) + 1):
            pos = tuple(map(sum, zip(pos, directions[i[0]])))
            n_steps += 1
            if pos in points:
                min_res = min(min_res, n_steps + steps_a[str(pos)])
    return min_res


def main(fn):
    with open("input", "r") as f:
        wire1 = f.readline().strip().split(',')
        wire2 = f.readline().strip().split(',')
    return fn(wire1, wire2)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

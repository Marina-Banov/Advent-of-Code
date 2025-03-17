import math


def part_one(estimate, buses):
    min_estimate = math.inf
    min_bus = 0
    for bus in buses:
        if (estimate // bus + 1) * bus < min_estimate:
            min_estimate = (estimate // bus + 1) * bus
            min_bus = bus
    return (min_estimate - estimate) * min_bus


def part_two(_estimate, _buses):
    return


def main(fn):
    with open("input", "r") as f:
        estimate = int(f.readline().strip())
        buses = list(map(int, filter(lambda a: a != 'x', f.readline().strip().split(','))))
    return fn(estimate, buses)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

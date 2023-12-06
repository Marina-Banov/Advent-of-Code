def part_one(line):
    return list(map(int, line.strip()[9:].split()))


def part_two(line):
    return [int(line.strip()[9:].replace(" ", ""))]


def main(parse_input):
    with open("input.txt", "r") as f:
        time = parse_input(f.readline())
        distance = parse_input(f.readline())
    res = 1
    for t, d in zip(time, distance):
        speed = d // t
        while speed * (t - speed) <= d:
            speed += 1
        peak = int(t / 2)
        res *= (peak - speed) * 2 + 1 + t % 2
    return res


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

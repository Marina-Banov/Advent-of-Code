def part_one(fuel):
    result = 0
    for f in fuel:
        result += int(f / 3) - 2
    return result


def part_two(fuel):
    result = 0
    for f in fuel:
        f = int(f / 3) - 2
        while f > 0:
            result += f
            f = int(f / 3) - 2
    return result


def main(fn):
    fuel = []
    with open("input", "r") as f:
        while True:
            try:
                fuel.append(int(f.readline().strip()))
            except Exception as _:
                break
    return fn(fuel)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

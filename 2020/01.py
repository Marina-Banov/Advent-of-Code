def part_one(entries):
    less = []
    more = []
    exact = 0
    for n in entries:
        if n > 1010:
            more.append(n)
        elif n < 1010:
            less.append(n)
        else:
            exact += 1
    if exact == 2:
        return 1010 * 1010
    for lt in sorted(less):
        for mt in sorted(more, reverse=True):
            if lt + mt == 2020:
                return lt * mt
            elif lt + mt < 2020:
                break


def part_two(entries):
    for x in range(len(entries)):
        for y in range(x + 1, len(entries)):
            for z in range(y + 1, len(entries)):
                if entries[x] + entries[y] + entries[z] == 2020:
                    return entries[x] * entries[y] * entries[z]


def main(fn):
    with open("input", "r") as f:
        entries = list(map(int, [line.strip() for line in f.readlines()]))
    return fn(entries)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

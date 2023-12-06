from math import inf


def loop_categories(seed, maps):
    cur = seed
    skip = inf
    for category in maps:
        for _map in category:
            if 0 <= cur - _map[1] < _map[2]:
                skip = min(skip, _map[1] + _map[2] - cur)
                cur = _map[0] + cur - _map[1]
                break
    return cur, skip


def part_one(seeds, maps):
    return min([loop_categories(s, maps)[0] for s in seeds])


def part_two(seeds, maps):
    min_location = inf
    for i in range(0, len(seeds), 2):
        seed = seeds[i]
        while seed < seeds[i] + seeds[i+1]:
            location, skip = loop_categories(seed, maps)
            min_location = min(min_location, location)
            seed += skip
    return min_location


def parse_input(lines):
    seeds = list(map(int, lines[0][7:].split()))
    del lines[0:3]
    maps = [[] for _ in range(7)]
    for category in range(7):
        i = 0
        while i < len(lines) and lines[i] != "":
            maps[category].append(list(map(int, lines[i].split())))
            i += 1
        if i < len(lines):
            del lines[0:i+2]
        else:
            del lines[:]
    return seeds, maps


def main(min_location):
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
    seeds, maps = parse_input(lines)
    return min_location(seeds, maps)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

def part_one(lines):
    all_sum = 0
    group = []
    for line in lines:
        if line == "":
            all_sum += len(group)
            group = []
            continue
        for letter in line:
            if not letter in group:
                group.append(letter)
    return all_sum


def part_two(lines):
    all_sum = 0
    group = []
    singles = []
    for line in lines:
        if line == "":
            n_passengers = len(group)
            group = sum(group, [])
            for s in singles:
                if group.count(s) == n_passengers:
                    all_sum += 1
            group = []
            singles = []
            continue
        for letter in line:
            if not letter in singles:
                singles.append(letter)
        group.append([letter for letter in line])
    return all_sum


def main(fn):
    with open("input", "r") as f:
        lines = f.read().strip().split("\n")
        lines.append("")
    return fn(lines)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

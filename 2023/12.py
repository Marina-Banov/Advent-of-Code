from itertools import combinations


def contiguous(arr, element):
    res = []
    n = 0
    for el in arr:
        if el == element:
            n += 1
        elif n > 0:
            res.append(n)
            n = 0
    if n > 0:
        res.append(n)
    return res


def perm(record, arrangement):
    n = record.count("?")
    h = record.count("#")
    if n + h == sum(arrangement):
        return 1
    res = 0
    for bits in combinations(range(n), sum(arrangement) - h):
        rep = ["."] * n
        for bit in bits:
            rep[bit] = "#"
        k = 0
        test = ""
        for el in record:
            if el == "?":
                test = test + rep[k]
                k += 1
            else:
                test = test + el
        if contiguous(test, "#") == arrangement:
            res += 1
    return res


def part_one(record, arrangement):
    return perm(record, arrangement)


def part_two(record, arrangement):
    return 0


def main(sum_el):
    res = 0
    with open("input.txt", "r") as f:
        while True:
            line = f.readline().strip()
            if line == "":
                break
            record, arrangement = line.split()
            arrangement = list(map(int, arrangement.split(",")))
            res += sum_el(record, arrangement)
    return res


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

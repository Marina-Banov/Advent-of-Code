def part_one(seq):
    _next = seq[-1]
    while any(seq):
        seq = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
        _next += seq[-1]
    return _next


def part_two(seq):
    seq.reverse()
    return part_one(seq)


def main(sum_el):
    res = 0
    with open("input.txt", "r") as f:
        while True:
            line = f.readline().strip()
            if line == "":
                break
            line = list(map(int, line.split()))
            res += sum_el(line)
    return res


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

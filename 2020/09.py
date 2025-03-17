def is_sum_of_two(n, preamble):
    s = set()
    for i in range(25):
        temp = n - preamble[i]
        if temp in s:
            return True
        s.add(preamble[i])
    return False


def part_one(numbers):
    for i in range(25, len(numbers)):
        if not is_sum_of_two(numbers[i], numbers[i - 25:i]):
            return numbers[i]


def part_two(numbers):
    invalid = part_one(numbers)
    chosen = []
    for i in numbers:
        chosen.append(i)
        j = 0
        while sum(chosen) > invalid:
            del chosen[j]
        if sum(chosen) == invalid:
            return min(chosen) + max(chosen)


def main(fn):
    with open("input", "r") as f:
        numbers = list(map(int, f.read().strip().split()))
    return fn(numbers)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

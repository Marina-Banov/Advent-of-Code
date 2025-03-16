def part_one(digits):
    return any([digit == digits[j + 1] for j, digit in enumerate(digits) if j < 5])


def part_two(digits):
    return any([digit for digit in set(digits) if digits.count(digit) == 2])


def main(fn):
    with open("input", "r") as f:
        start, end = f.readline().strip().split('-')
    count = 0
    i = int(start)
    while i < int(end):
        digits = list(str(i))
        factor = 10000
        flag = False
        for j in range(5):
            if digits[j] > digits[j + 1]:
                i = int((i + factor) / factor) * factor
                flag = True
                break
            factor = int(factor / 10)
        if flag:
            continue
        if fn(digits):
            count += 1
        i += 1
    return count


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

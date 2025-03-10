import re
from utils import DIGITS_MAP


def part_one(line):
    return list(map(int, re.findall(r"\d", line)))


def part_two(line):
    return list(map(
        lambda s: DIGITS_MAP[s] if s in DIGITS_MAP.keys() else int(s),
        re.findall(rf"(?=({'|'.join(DIGITS_MAP.keys())}|\d))", line)
    ))


def main(gen_digits):
    res = 0
    with open("input.txt", "r") as f:
        while True:
            line = f.readline().strip()
            if line == "":
                break
            digits = gen_digits(line)
            res += digits[0] * 10 + digits[-1]
    return res


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

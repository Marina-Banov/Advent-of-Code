import re


def part_one(line):
    return list(map(int, re.findall(r"\d", line)))


def part_two(line):
    digits_map = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    }
    return list(map(
        lambda s: digits_map[s] if s in digits_map.keys() else int(s),
        re.findall(f"(?=({'|'.join(digits_map.keys())}|\d))", line)
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

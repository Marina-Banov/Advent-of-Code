def part_one(a, b, letter, password):
    pl = password.count(letter)
    return int(b) >= pl >= int(a)


def part_two(a, b, letter, password):
    p1 = password[int(a) - 1] == letter
    p2 = password[int(b) - 1] == letter
    return (p1 or p2) and not (p1 and p2)


def main(fn):
    valid = 0
    with open("input", "r") as f:
        while True:
            n = f.readline().strip()
            if n == '':
                break
            a, password = n.split('-')
            b, letter, password = password.split(' ')
            letter = letter.strip(':')
            valid += fn(a, b, letter, password)
    return valid


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

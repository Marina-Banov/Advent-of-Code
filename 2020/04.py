import re


class Passport:
    def __init__(self):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None


def valid_hgt(hgt):
    if hgt[-2:] == "in":
        return 59 <= int(hgt[:-2]) <= 76
    if hgt[-2:] == "cm":
        return 150 <= int(hgt[:-2]) <= 193
    return False


def part_one(p):
    return None not in [p.byr, p.iyr, p.eyr, p.hgt, p.hcl, p.ecl, p.pid]


def part_two(p):
    if not part_one(p):
        return False
    if not 1920 <= int(p.byr) <= 2002:
        return False
    if not 2010 <= int(p.iyr) <= 2020:
        return False
    if not 2020 <= int(p.eyr) <= 2030:
        return False
    if not valid_hgt(p.hgt):
        return False
    if not re.match(r"^#[a-f\d]{6}$", p.hcl):
        return False
    if p.ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if not re.match(r"^\d{9}$", p.pid):
        return False
    return True


def main(fn):
    with open("input", "r") as f:
        content = f.read().strip().split("\n")
        content.append("")
    valid = 0
    p = Passport()
    for c in content:
        if c == "":
            valid += fn(p)
            p = Passport()
            continue
        c = c.split(' ')
        for j in c:
            key, value = j.split(':')
            setattr(p, key, value)
    return valid


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

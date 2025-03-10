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

    def valid_hgt(self):
        if self.hgt[-2:] == "in":
            return int(self.hgt[:-2]) >= 59 and int(self.hgt[:-2]) <= 76
        if self.hgt[-2:] == "cm":
            return int(self.hgt[:-2]) >= 150 and int(self.hgt[:-2]) <= 193
        return False

    def is_valid(self):
        if self.byr is None or int(self.byr) < 1920 or int(self.byr) > 2002:
            return 0
        if self.iyr is None or int(self.iyr) < 2010 or int(self.iyr) > 2020:
            return 0
        if self.eyr is None or int(self.eyr) < 2020 or int(self.eyr) > 2030:
            return 0
        if self.hgt is None or not self.valid_hgt():
            return 0
        if self.hcl is None or not re.match(r"^#[a-f\d]{6}$", self.hcl):
            return 0
        if self.ecl is None or self.ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return 0
        if self.pid is None or not re.match(r"^\d{9}$", self.pid):
            return 0
        return 1


content = open("input.txt", 'r').read().strip().split("\n")
content.append("")
valid = 0
p = Passport()

for i in range(len(content)):
    if content[i] == "":
        valid += p.is_valid()
        p = Passport()
        continue
    content[i] = content[i].split(' ')
    for j in content[i]:
        key, value = j.split(':')
        setattr(p, key, value)

print(valid)

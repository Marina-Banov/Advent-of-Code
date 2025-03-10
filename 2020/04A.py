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

    def is_valid(self):
        if self.byr is None:
            return 0
        if self.iyr is None:
            return 0
        if self.eyr is None:
            return 0
        if self.hgt is None:
            return 0
        if self.hcl is None:
            return 0
        if self.ecl is None:
            return 0
        if self.pid is None:
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

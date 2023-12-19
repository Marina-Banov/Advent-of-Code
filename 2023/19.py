import re


def f(c, r, n, p):
    return p[c] != int(n) and (p[c] < int(n)) ^ (r == ">")


def eval(workflows, w, part):
    if w == "R":
        return False
    if w == "A":
        return True
    i = 0
    while i < len(workflows[w]):
        if ":" not in workflows[w][i]:
            return eval(workflows, workflows[w][i], part)
        rule = re.match(r"(?P<c>\w)(?P<r>.?)(?P<n>\d+):(?P<w>\w+)", workflows[w][i])
        if f(rule["c"], rule["r"], rule["n"], part):
            return eval(workflows, rule["w"], part)
        i += 1
    return False


def part_one(rules, parts):
    return sum([sum(p[i] for i in "xmas") for p in parts if eval(rules, "in", p)])


def part_two(rules, _):
    return


def get_rule(s):
    workflow = re.match(r"(?P<w>\w+){(?P<s>.+)}", s)
    return workflow["w"], workflow["s"].split(",")


def get_part(s):
    categories = re.match(r"{x=(?P<x>\d+),m=(?P<m>\d+),a=(?P<a>\d+),s=(?P<s>\d+)}", s)
    return {i: int(categories[i]) for i in "xmas"}


def main(res):
    with open("input.txt", "r") as f:
        rules = {}
        while True:
            line = f.readline().strip()
            if line == "":
                break
            k, v = get_rule(line)
            rules[k] = v
        parts = [get_part(line.strip()) for line in f.readlines()]
    return res(rules, parts)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

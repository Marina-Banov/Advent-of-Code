from math import lcm
import re


class Module:
    def __init__(self, line):
        self.state = False
        self.src = {}
        m = re.match(r"(?P<type>([%&])?)(?P<name>\w+) -> (?P<dst>.*)", line)
        self.type = m["type"]
        self.name = m["name"]
        self.dst = m["dst"].split(", ")

    def __eq__(self, other):
        return self.name == other.name

    def recieve_pulse(self, pulse, src):
        if self.type == "%":
            if pulse == False:
                self.state = not self.state
                return [(self.state, d, self.name) for d in self.dst]
        elif self.type == "&":
            self.src[src] = pulse
            return [(not all(self.src.values()), d, self.name) for d in self.dst]
        else:
            return [(pulse, d, self.name) for d in self.dst]
        return []


def push(modules):
    steps = [(False, "broadcaster", "button")]
    stack = [*modules["broadcaster"].recieve_pulse(False, "button")]
    while len(stack):
        pulse, dst, src = stack.pop(0)
        steps.append((pulse, dst, src))
        if dst in modules:
            stack.extend(modules[dst].recieve_pulse(pulse, src))
    return steps


def part_one(modules):
    high = 0
    low = 0
    for i in range(1, 1001):
        steps = push(modules)
        high += sum([1 for step in steps if step[0]])
        low += sum([1 for step in steps if not step[0]])
        if not any([m.state for m in modules.values() if m.type == "%"]):
            break
    return high * low * (1000 // i) ** 2


def part_two(modules):
    input_modules = ["rx"]
    while len(input_modules) == 1:
        dst = input_modules.pop()
        input_modules = [m for m in modules if dst in modules[m].dst]
    cycles = {m: 0 for m in input_modules}
    i = 1
    while not all(cycles.values()):
        steps = push(modules)
        for step in steps:
            if step[0] and step[2] in input_modules and not cycles[step[2]]:
                cycles[step[2]] = i
        i += 1
    return lcm(*cycles.values())


def main(res):
    with open("input.txt", "r") as f:
        modules = [Module(line.strip()) for line in f.readlines()]
    conj = [i for i, m in enumerate(modules) if m.type == "&"]
    for c in conj:
        modules[c].src = {m.name: False for m in modules if modules[c].name in m.dst}
    modules = {m.name: m for m in modules}
    return res(modules)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

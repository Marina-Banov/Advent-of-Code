from enum import Enum


class Instruction(Enum):
    NONE = 0
    ADD = 1
    MULTIPLY = 2


class Program:
    def __init__(self, ints, Instruction=Instruction):
        Program.Instruction = Instruction
        self.ints = ints
        self.i = 0

    def perform_operation(self, instruction, op_a, op_b, op_c):
        if instruction == Program.Instruction.ADD:
            self.ints[op_a] = self.ints[op_c] + self.ints[op_b]
        if instruction == Program.Instruction.MULTIPLY:
            self.ints[op_a] = self.ints[op_c] * self.ints[op_b]

    def run(self):
        while self.ints[self.i] != 99:
            op_a = self.ints[self.i+3]
            op_b = self.ints[self.i+2]
            op_c = self.ints[self.i+1]
            self.perform_operation(Program.Instruction(self.ints[self.i]), op_a, op_b, op_c)
            self.i += 4


def part_one(ints):
    p = Program(ints)
    p.ints[1] = 12
    p.ints[2] = 2
    p.run()
    return p.ints[0]


def part_two(ints):
    pairs = []
    for i in range(len(ints)-1):
        for j in range(i, len(ints)):
            pairs.append((i, j))
    while True:
        a, b = pairs.pop()
        p = Program(ints[:])
        p.ints[1] = a
        p.ints[2] = b
        p.run()
        if p.ints[0] == 19690720:
            return 100 * a + b


def main(fn):
    with open("input", "r") as f:
        ints = list(map(int, f.readline().strip().split(",")))
    return fn(ints)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

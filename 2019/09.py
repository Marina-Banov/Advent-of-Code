from enum import Enum

day5 = __import__("05")


class Instruction(Enum):
    NONE = 0
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    RELATIVE_BASE = 9


class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class Program(day5.Program):
    def __init__(self, ints, inputs, Instruction=Instruction, Mode=Mode):
        super().__init__(ints, inputs, Instruction, Mode)
        self.relative_base = 0

    def get_operand(self, mode, offset):
        if mode == Program.Mode.POSITION:
            self.expand_memory(self.ints[self.i + offset])
            return self.ints[self.i + offset]
        if mode == Program.Mode.IMMEDIATE:
            return self.i + offset
        if mode == Program.Mode.RELATIVE:
            self.expand_memory(self.ints[self.i + offset] + self.relative_base)
            return self.ints[self.i + offset] + self.relative_base

    def expand_memory(self, limit):
        if limit >= len(self.ints) and limit < 1_000_000:
            cpy = [0 for j in range(limit + 1)]
            cpy[:len(self.ints)] = self.ints[:]
            self.ints = cpy

    def run(self):
        while self.ints[self.i] != 99:
            instruction, operands = self.interpret()

            if instruction == Program.Instruction.INPUT:
                self.ints[operands[2]] = self.inputs
                self.i += 2
            elif instruction == Program.Instruction.OUTPUT:
                self.res.append(self.ints[operands[2]])
                self.i += 2
            elif instruction == Program.Instruction.RELATIVE_BASE:
                self.relative_base += self.ints[operands[2]]
                self.i += 2
            else:
                self.i = self.perform_operation(instruction, *operands)


def part_one(ints):
    p = Program(ints, 1)
    p.run()
    return p.res[0]


def part_two(ints):
    p = Program(ints, 2)
    p.run()
    return p.res[0]


def main(fn):
    with open("input", "r") as f:
        ints = list(map(int, f.readline().strip().split(',')))
    return fn(ints)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

from enum import Enum

day2 = __import__("02")


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


class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1


class Program(day2.Program):
    def __init__(self, ints, inputs, Instruction=Instruction, Mode=Mode):
        super().__init__(ints, Instruction)
        Program.Mode = Mode
        self.inputs = inputs
        self.res = []

    def get_operand(self, mode, offset):
        if mode == Program.Mode.POSITION:
            return self.ints[self.i + offset]
        if mode == Program.Mode.IMMEDIATE:
            return self.i + offset

    def interpret(self):
        opcode = str(self.ints[self.i]).zfill(5)
        op_c = self.get_operand(Program.Mode(int(opcode[2])), 1)
        op_b = self.get_operand(Program.Mode(int(opcode[1])), 2)
        op_a = self.get_operand(Program.Mode(int(opcode[0])), 3)
        return Program.Instruction(int(opcode[4])), (op_a, op_b, op_c)

    def perform_operation(self, instruction, op_a, op_b, op_c):
        if instruction == Program.Instruction.ADD:
            self.ints[op_a] = self.ints[op_c] + self.ints[op_b]

        if instruction == Program.Instruction.MULTIPLY:
            self.ints[op_a] = self.ints[op_c] * self.ints[op_b]

        if instruction == Program.Instruction.JUMP_IF_TRUE:
            return self.ints[op_b] if self.ints[op_c] != 0 else self.i + 3

        if instruction == Program.Instruction.JUMP_IF_FALSE:
            return self.ints[op_b] if self.ints[op_c] == 0 else self.i + 3

        if instruction == Program.Instruction.LESS_THAN:
            self.ints[op_a] = 1 if self.ints[op_c] < self.ints[op_b] else 0

        if instruction == Program.Instruction.EQUALS:
            self.ints[op_a] = 1 if self.ints[op_c] == self.ints[op_b] else 0

        return self.i + 4

    def run(self):
        while self.ints[self.i] != 99:
            instruction, operands = self.interpret()

            if instruction == Program.Instruction.INPUT:
                self.ints[operands[2]] = self.inputs
                self.i += 2
            elif instruction == Program.Instruction.OUTPUT:
                self.res.append(self.ints[operands[2]])
                self.i += 2
            else:
                self.i = self.perform_operation(instruction, *operands)


def part_one(ints):
    p = Program(ints, 1)
    p.run()
    return p.res[-1]


def part_two(ints):
    p = Program(ints, 5)
    p.run()
    return p.res[0]


def main(fn):
    with open("input", "r") as f:
        ints = list(map(int, f.readline().strip().split(',')))
    return fn(ints)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

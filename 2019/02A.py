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


def main():
    f = open("input.txt", 'r')
    ints = list(map(int, f.readline().strip().split(",")))
    p = Program(ints)
    p.ints[1] = 12
    p.ints[2] = 2
    p.run()
    print(p.ints[0])


if __name__ == "__main__":
    main()

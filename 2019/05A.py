from enum import Enum
day2 = __import__("02A")


class Instruction(Enum):
    NONE = 0
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4


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
                self.perform_operation(instruction, *operands)
                self.i += 4


def main():
    f = open("input.txt", 'r')
    ints = list(map(int, f.readline().strip().split(',')))
    p = Program(ints, 1)
    p.run()
    print(p.res[-1])


if __name__ == "__main__":
    main()

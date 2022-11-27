from enum import Enum
day5 = __import__("05A")


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


class Program(day5.Program):
    def __init__(self, ints, inputs, Instruction=Instruction, Mode=day5.Mode):
        super().__init__(ints, inputs, Instruction, Mode)

    def perform_operation(self, instruction, op_a, op_b, op_c):
        if instruction == Program.Instruction.ADD:
            self.ints[op_a] = self.ints[op_c] + self.ints[op_b]
        
        if instruction == Program.Instruction.MULTIPLY:
            self.ints[op_a] = self.ints[op_c] * self.ints[op_b]
        
        if instruction == Program.Instruction.JUMP_IF_TRUE:
            return self.ints[op_b] if self.ints[op_c] != 0 else self.i+3
        
        if instruction == Program.Instruction.JUMP_IF_FALSE:
            return self.ints[op_b] if self.ints[op_c] == 0 else self.i+3
        
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


def main():
    f = open("input.txt", 'r')
    ints = list(map(int, f.readline().strip().split(',')))
    p = Program(ints, 5)
    p.run()
    print(p.res[0])


if __name__ == "__main__":
    main()

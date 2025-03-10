import itertools
day7 = __import__("07A")


class Program(day7.Program):
    def __init__(self, ints, inputs):
        super().__init__(ints, inputs)
        self.done = False

    def interpret(self):
        opcode = str(self.ints[self.i]).zfill(5)
        op_c = self.get_operand(Program.Mode(int(opcode[2])), 1)
        op_b = self.get_operand(Program.Mode(int(opcode[1])), 2)
        try:
            op_a = self.get_operand(Program.Mode(int(opcode[0])), 3)
        except IndexError as _:
            op_a = None
        return Program.Instruction(int(opcode[4])), (op_a, op_b, op_c)

    def run(self):
        while True:
            if self.ints[self.i] == 99:
                self.done = True
                return None
            instruction, operands = self.interpret()

            if instruction == Program.Instruction.INPUT:
                if self.inputs_i == len(self.inputs):
                    return None
                self.ints[self.ints[self.i+1]] = self.inputs[self.inputs_i]
                self.inputs_i += 1
                self.i += 2
            elif instruction == Program.Instruction.OUTPUT:
                self.res.append(self.ints[operands[2]])
                self.i += 2
                return
            else:
                self.i = self.perform_operation(instruction, *operands)


def main():
    f = open("input.txt", 'r')
    ints = list(map(int, f.readline().strip().split(',')))
    max_r = 0

    for settings in list(itertools.permutations([5, 6, 7, 8, 9])):
        programs = []
        for s in list(settings): 
            programs.append(Program(ints[:], [s]))

        cur_prog = 0
        next_input = 0
        while not all([p.done for p in programs]):
            if next_input is not None:
                programs[cur_prog].inputs.append(next_input)
            programs[cur_prog].run()
            next_input = programs[cur_prog].res[-1]
            cur_prog = (cur_prog + 1) % 5

        max_r = max(max_r, programs[4].res[-1])

    print(max_r)


if __name__ == "__main__":
    main()

import itertools
day5 = __import__("05B")


class Program(day5.Program):
    def __init__(self, ints, inputs):
        super().__init__(ints, inputs)
        self.inputs_i = 0

    def run(self):
        while self.ints[self.i] != 99:
            instruction, operands = self.interpret()

            if instruction == Program.Instruction.INPUT:
                self.ints[operands[2]] = self.inputs[self.inputs_i]
                if self.inputs_i < len(self.inputs)-1:
                    self.inputs_i += 1
                self.i += 2
            elif instruction == Program.Instruction.OUTPUT:
                self.res.append(self.ints[operands[2]])
                return
            else:
                self.i = self.perform_operation(instruction, *operands)


def main():
    f = open("input.txt", 'r')
    ints = list(map(int, f.readline().strip().split(',')))
    max_r = 0

    for settings in list(itertools.permutations([0, 1, 2, 3, 4])):
        res = 0
        for i in list(settings):
            p = Program(ints[:], [i, res])
            p.run()
            res = p.res[-1]
        max_r = max(max_r, res)

    print(max_r)


if __name__ == "__main__":
    main()

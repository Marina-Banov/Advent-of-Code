day9 = __import__("09")


class Program(day9.Program):
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
            elif instruction == Program.Instruction.RELATIVE_BASE:
                self.relative_base += self.ints[operands[2]]
                self.i += 2
            else:
                self.i = self.perform_operation(instruction, *operands)

    def restart(self, ints, inputs):
        self.ints = ints
        self.i = 0
        self.inputs = inputs
        self.inputs_i = 0
        self.relative_base = 0
        self.res = []


def part_one(ints):
    grid = [[None for _ in range(50)] for _ in range(50)]
    p = Program(ints[:], None)
    for i in range(50):
        for j in range(50):
            p.restart(ints[:], [i, j])
            p.run()
            grid[i][j] = p.res[0]
    return sum([row.count(1) for row in grid])


def part_two(_):
    return


def main(fn):
    with open("input", "r") as f:
        ints = list(map(int, f.readline().strip().split(',')))
    return fn(ints)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

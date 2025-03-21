day9 = __import__("09")


class Program(day9.Program):
    def __init__(self, ints, inputs):
        super().__init__(ints, inputs)
        self.res = ""

    def run(self):
        while self.ints[self.i] != 99:
            instruction, operands = self.interpret()

            if instruction == Program.Instruction.INPUT:
                self.ints[operands[2]] = self.inputs
                self.i += 2
            elif instruction == Program.Instruction.OUTPUT:
                self.res += chr(self.ints[operands[2]])
                self.i += 2
            elif instruction == Program.Instruction.RELATIVE_BASE:
                self.relative_base += self.ints[operands[2]]
                self.i += 2
            else:
                self.i = self.perform_operation(instruction, *operands)


ADJACENT = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]


def part_one(ints):
    p = Program(ints, None)
    p.run()
    view = [list(row) for row in p.res.split()]
    res = 0
    for i in range(1, len(view) - 1):
        for j in range(1, len(view[0]) - 1):
            adjacent = [view[i + a[0]][j + a[1]] for a in ADJACENT]
            if all([el == '#' for el in adjacent]):
                res += i * j
    return res


def part_two(_):
    return


def main(fn):
    with open("input", "r") as f:
        ints = list(map(int, f.readline().strip().split(',')))
    return fn(ints)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

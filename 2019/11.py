day9 = __import__("09")


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Program(day9.Program):
    def __init__(self, ints, inputs):
        super().__init__(ints, inputs)
        self.x = 50
        self.y = 50
        self.color = True
        self.direction = 0
        self.visited = set()

    def rotate(self, right):
        self.direction = (self.direction + (1 if right else -1)) % 4
        self.x += DIRECTIONS[self.direction][0]
        self.y += DIRECTIONS[self.direction][1]

    def run(self):
        while self.ints[self.i] != 99:
            instruction, operands = self.interpret()

            if instruction == Program.Instruction.INPUT:
                self.ints[operands[2]] = self.inputs[self.y][self.x]
                self.i += 2
            elif instruction == Program.Instruction.OUTPUT:
                if self.color:
                    self.inputs[self.y][self.x] = self.ints[operands[2]]
                    self.visited.add((self.x, self.y))
                else:
                    self.rotate(self.ints[operands[2]] == 1)
                self.i += 2
                self.color = not self.color
            elif instruction == Program.Instruction.RELATIVE_BASE:
                self.relative_base += self.ints[operands[2]]
                self.i += 2
            else:
                self.i = self.perform_operation(instruction, *operands)


def part_one(ints):
    p = Program(ints, [[0 for _ in range(100)] for _ in range(100)])
    p.run()
    return len(p.visited)


def part_two(ints):
    tiles = [[0 for _ in range(100)] for _ in range(100)]
    tiles[50][50] = 1
    p = Program(ints, tiles)
    p.run()
    white_tiles = [(i, j) for j in range(len(p.inputs)) for i, val in enumerate(p.inputs[j]) if val == 1]
    min_x = min(tile[1] for tile in white_tiles)
    min_y = min(tile[0] for tile in white_tiles)
    max_x = max(tile[1] for tile in white_tiles)
    max_y = max(tile[0] for tile in white_tiles)
    res = [['#' if (i, j) in white_tiles else ' ' for i in range(min_y, max_y + 1)] for j in range(min_x, max_x + 1)]
    res = map(list, zip(*res))
    s = ""
    for row in res:
        s = s + "".join(row) + "\n"
    return s


def main(fn):
    with open("input", "r") as f:
        ints = list(map(int, f.readline().strip().split(',')))
    return fn(ints)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

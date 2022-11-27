day9 = __import__("09A")


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
        

def main():
    f = open("input.txt", 'r')
    ints = list(map(int, f.readline().strip().split(',')))
    p = Program(ints, [[0 for i in range(100)] for j in range(100)])
    p.run()
    print(len(p.visited))


if __name__ == "__main__":
    main()

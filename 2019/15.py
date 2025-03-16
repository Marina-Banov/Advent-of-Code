day9 = __import__("09")


TILES = ['#', '.', 'O', ' ']
RULES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def opposite_direction(direction):
    return direction-1 if (direction % 2 == 1) else direction+1


class Graph:
    def __init__(self, size, pos):
        self.size_x, self.size_y = size
        self.x, self.y = pos
        self.area = [[" " for j in range(self.size_x)] for i in range(self.size_y)]
        self.area[self.y][self.x] = 'x'
        self.adjacency_list = self.create_adjacency_list()
        self.stack = []
        self.target = None
        self.visited = [[False for _ in range(self.size_x)] for _ in range(self.size_y)]

    def create_adjacency_list(self):
        res = [[[] for j in range(self.size_x)] for i in range(self.size_y)]
        for i in range(self.size_y):
            for j in range(self.size_x):
                adjacent = []
                for idx, rule in enumerate(RULES):
                    a = i + rule[0]
                    b = j + rule[1]
                    if 0 <= a < self.size_y and 0 <= b < self.size_x and self.area[a][b] != '#':
                        adjacent.append(idx)
                res[i][j] = adjacent
        return res

    def dfs_depth(self, source, depth):
        i, j = source
        if self.visited[i][j]:
            return depth-1

        self.visited[i][j] = True
        neighbors = [(i + RULES[n][0], j + RULES[n][1]) for n in self.adjacency_list[i][j]]

        return max([self.dfs_depth(n, depth+1) for n in neighbors])

    def dfs_strategy(self):
        adjacency_list = self.adjacency_list[self.y][self.x]
        if len(adjacency_list) == 0:
            # All possible paths from the current position have been explored,
            # return to previous position.
            # If stack is empty (we have returned to the initial position),
            # this line will raise an exception, which means the program should halt.
            return self.stack.pop()

        if len(self.stack) == 0:
            # First step, start exploring.
            self.stack.append(opposite_direction(adjacency_list[0]))
            return adjacency_list[0]

        prev_direction = self.stack[-1]
        try:
            # Do not allow returning to this position from previous (avoid loops)
            _y = self.y + RULES[prev_direction][0]
            _x = self.x + RULES[prev_direction][1]
            self.adjacency_list[_y][_x].remove(opposite_direction(prev_direction))
        except Exception as _:
            pass

        other_directions = [d for d in adjacency_list if d != prev_direction]
        if len(other_directions) > 0:
            # If possible, explore different directions/paths
            self.stack.append(opposite_direction(other_directions[0]))
            return other_directions[0]

        # Only return to previous position if there are no other options
        self.stack.pop()
        return prev_direction

    def bfs(self, source):
        self.stack = [source]
        self.adjacency_list = self.create_adjacency_list()
        visited = [source]
        parent = [[None for j in range(self.size_x)] for i in range(self.size_y)]

        while self.stack:
            i, j = self.stack.pop(0)

            if (i, j) == self.target:
                break

            for n in self.adjacency_list[i][j]:
                neighbour = (i + RULES[n][0], j + RULES[n][1])
                if neighbour not in visited:
                    visited.append(neighbour)
                    parent[neighbour[0]][neighbour[1]] = (i, j)
                    self.stack.append(neighbour)

        path = [(i, j)]
        while parent[i][j] != source:
            path.append(parent[i][j])
            i, j = parent[i][j]
        path.reverse()
        # print(path)
        return len(path)

    def set_adjacent_area(self, d, result):
        direction = RULES[d]
        result = TILES[result]
        if result == '#':
            self.area[self.y + direction[0]][self.x + direction[1]] = result
            self.stack.pop()
            self.adjacency_list[self.y][self.x].remove(d)
        else:
            self.y += direction[0]
            self.x += direction[1]
            if self.area[self.y][self.x] == ' ':
                self.area[self.y][self.x] = result
            if result == 'O':
                self.target = (self.y, self.x)

    def __repr__(self):
        string = ""
        for row in self.area:
            string += "".join(row) + "\n"
        return string


class Program(day9.Program):
    def __init__(self, ints, inputs):
        super().__init__(ints, inputs)

    def run(self, graph):
        while self.ints[self.i] != 99:
            instruction, operands = self.interpret()

            if instruction == Program.Instruction.INPUT:
                try:
                    self.inputs = graph.dfs_strategy()
                except IndexError as _:
                    break
                self.ints[operands[2]] = self.inputs+1
                self.i += 2
            elif instruction == Program.Instruction.OUTPUT:
                graph.set_adjacent_area(self.inputs, self.ints[operands[2]])
                self.i += 2
            elif instruction == Program.Instruction.RELATIVE_BASE:
                self.relative_base += self.ints[operands[2]]
                self.i += 2
            else:
                self.i = self.perform_operation(instruction, *operands)


def part_one(ints):
    p = Program(ints, None)
    graph = Graph((41, 41), (21, 21))
    p.run(graph)
    # print(graph)
    return graph.bfs((21, 21))


def part_two(ints):
    p = Program(ints, None)
    graph = Graph((41, 41), (21, 21))
    p.run(graph)
    # print(graph)
    graph.adjacency_list = graph.create_adjacency_list()
    return graph.dfs_depth(graph.target, 0)


def main(fn):
    with open("input", "r") as f:
        ints = list(map(int, f.readline().strip().split(',')))
    return fn(ints)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

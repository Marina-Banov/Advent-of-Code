day15 = __import__("15A")


class Graph(day15.Graph):
    def __init__(self, size, pos):
        super().__init__(size, pos)
        self.visited = [[False for _ in range(self.size_x)] for _ in range(self.size_y)]

    def dfs_depth(self, source, depth):
        i, j = source
        if self.visited[i][j]:
            return depth-1

        self.visited[i][j] = True
        neighbors = [(i + day15.RULES[n][0], j + day15.RULES[n][1]) for n in self.adjacency_list[i][j]]

        return max([self.dfs_depth(n, depth+1) for n in neighbors])


def main():
    f = open("input.txt", 'r')
    ints = list(map(int, f.readline().strip().split(',')))
    p = day15.Program(ints, None)
    graph = Graph((41, 41), (21, 21))
    p.run(graph)
    # print(graph)
    graph.adjacency_list = graph.create_adjacency_list()
    print(graph.dfs_depth(graph.target, 0))


if __name__ == "__main__":
    main()

class Node:
    def __init__(self, parent=None, position=None, end_position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = abs(position[0] - end_position[0]) + abs(position[1] - end_position[1])
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    start_node = Node(None, start, end)
    end_node = Node(None, end, end)

    open_list = [start_node]
    closed_list = []

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        if current_node in closed_list:
            continue
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not start_node:
                path.append(maze[current.position[0]][current.position[1]])
                current = current.parent
            return path[::-1]

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if not 0 <= node_position[0] < len(maze) or \
                    not 0 <= node_position[1] < len(maze[0]):
                continue

            child = Node(current_node, node_position, end_node.position)

            if child in closed_list:
                continue

            child.g = current_node.g + maze[child.position[0]][child.position[1]]
            child.f = child.g + child.h

            try:
                child_index = open_list.index(child)
                if open_list[child_index].f > child.f:
                    open_list[child_index] = child
            except ValueError:
                open_list.append(child)


def main():
    with open("input.txt", 'r') as f:
        maze = [list(map(int, list(line.strip()))) for line in f.readlines()]

    start = (0, 0)
    end = (len(maze)-1, len(maze[0])-1)

    path = astar(maze, start, end)
    print(sum(path))


if __name__ == "__main__":
    main()

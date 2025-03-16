def get_node(name, nodes):
    for n in nodes:
        if n.name == name:
            return n, False, True
        node_a = n.find_child(name)
        if node_a is not None:
            return node_a, False, False
    return Node(name), True, False


class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def get_depth(self, depth):
        res = depth
        for child in self.children:
            res += child.get_depth(depth + 1)
        return res

    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
            else:
                grandchild = child.find_child(name)
                if grandchild:
                    return grandchild
        return None


def part_one(nodes):
    return nodes[0].get_depth(0)


def part_two(nodes):
    src, _, _ = get_node("YOU", nodes)
    dst, _, _ = get_node("SAN", nodes)
    stack_src = []
    while src.name != "COM":
        src = src.parent
        stack_src.append(src.name)
    steps = 0
    while True:
        try:
            index = stack_src.index(dst.name)
            return steps + index - 1
        except Exception as _:
            steps += 1
            dst = dst.parent


def main(fn):
    nodes = [Node("COM")]
    with open("input", "r") as f:
        while True:
            try:
                name_a, name_b = f.readline().strip().split(')')
                node_a, should_add, _ = get_node(name_a, nodes)
                if should_add:
                    nodes.append(node_a)
                node_b, _, should_remove = get_node(name_b, nodes)
                if should_remove:
                    nodes.remove(node_b)
                node_a.children.append(node_b)
                node_b.parent = node_a
            except Exception as _:
                break
    return fn(nodes)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

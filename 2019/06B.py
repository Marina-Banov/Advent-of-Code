def get_node(name):
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

    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
            else:
                grandchild = child.find_child(name)
                if grandchild:
                    return grandchild
        return None


f = open("input.txt", 'r')

CENTER_OF_MASS = "COM"
nodes = [Node(CENTER_OF_MASS)]
src_name = "YOU"
dest_name = "SAN"
src = None
dest = None

while True:
    try:
        name_a, name_b = f.readline().strip().split(')')

        node_a, should_add, _ = get_node(name_a)
        if should_add:
            nodes.append(node_a)

        node_b, _, should_remove = get_node(name_b)
        if should_remove:
            nodes.remove(node_b)

        if name_b == src_name:
            src = node_b
        elif name_b == dest_name:
            dest = node_b

        node_a.children.append(node_b)
        node_b.parent = node_a
    except Exception as e:
        break

stack_src = []
while src.name != CENTER_OF_MASS:
    src = src.parent
    stack_src.append(src.name)

steps = 0
while True:
    try:
        index = stack_src.index(dest.name)
        break
    except Exception as e:
        steps += 1
        dest = dest.parent
    
print(steps + index - 1)

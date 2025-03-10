class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def get_depth(self, depth):
        res = depth
        for child in self.children:
            res += child.get_depth(depth+1)
        return res


f = open("input.txt", 'r')

root = Node("COM")
nodes = [root]

while True:
    try:
        name_a, name_b = f.readline().strip().split(')')

        node_a = next((n for n in nodes if n.name == name_a), None)
        if not node_a:
            node_a = Node(name_a)
            nodes.append(node_a)

        node_b = next((n for n in nodes if n.name == name_b), None)
        if not node_b:
            node_b = Node(name_b)
            nodes.append(node_b)

        node_a.children.append(node_b)
    except Exception as e:
        del nodes
        break

print(root.get_depth(0))

import math


class Node():
    def __init__(self, left=None, right=None):
        self.left = left
        if isinstance(left, Node):
            self.left.parent = self
        self.right = right
        if isinstance(right, Node):
            self.right.parent = self
        self.parent = None

    def magnitude(self):
        l = self.left.magnitude() if isinstance(self.left, Node) else self.left
        r = self.right.magnitude() if isinstance(self.right, Node) else self.right
        return 3 * l + 2 * r

    def height(self, h=0):
        res = None
        if isinstance(self.left, int) and isinstance(self.right, int) and h >= 4:
            return h, self
        if isinstance(self.right, Node):
            hr, r = self.right.height(h+1)
            res = r if r is not None else res
        else:
            hr = h
        if isinstance(self.left, Node):
            hl, r = self.left.height(h+1)
            res = r if r is not None else res
        else:
            hl = h
        return max(hr, hl), res

    def should_split(self):
        # find leftmost node to split
        if isinstance(self.left, int) and self.left >= 10:
            return self
        if isinstance(self.left, Node):
            n = self.left.should_split()
            if n is not None:
                return n

        if isinstance(self.right, int) and self.right >= 10:
            return self
        if isinstance(self.right, Node):
            return self.right.should_split()

        return None

    def predecessor(self):
        tmp = self.parent
        node = self
        while node is tmp.left:
            node = tmp
            tmp = tmp.parent
            if tmp is None:
                return
        if isinstance(tmp.left, int):
            tmp.left += self.left
        else:
            tmp = tmp.left
            while isinstance(tmp.right, Node):
                tmp = tmp.right
            tmp.right += self.left

    def successor(self):
        tmp = self.parent
        node = self
        while node is tmp.right:
            node = tmp
            tmp = tmp.parent
            if tmp is None:
                return
        if isinstance(tmp.right, int):
            tmp.right += self.right
        else:
            tmp = tmp.right
            while isinstance(tmp.left, Node):
                tmp = tmp.left
            tmp.left += self.right

    def __repr__(self):
        return f'[{self.left},{self.right}]'


def create_node(string):
    stack = []

    for i in range(len(string)):
        try:
            stack.append(int(string[i]))
        except ValueError as e:
            stack.append(string[i])
        if string[i] == ']':
            stack.pop()
            right = stack.pop()
            stack.pop()
            left = stack.pop()
            stack.pop()
            n = Node(left, right)
            stack.append(n)

    return stack[0]


def reduce_snail_number(root):
    while True:
        _, explode_node = root.height()
        if explode_node is not None:
            explode_node.predecessor()
            explode_node.successor()
            if explode_node is explode_node.parent.left:
                explode_node.parent.left = 0
            else:
                explode_node.parent.right = 0
            continue

        split_node = root.should_split()
        if split_node is not None:
            if isinstance(split_node.left, int) and split_node.left >= 10:
                n = Node(math.floor(split_node.left / 2), math.ceil(split_node.left / 2))
                split_node.left = n
            else:
                n = Node(math.floor(split_node.right / 2), math.ceil(split_node.right / 2))
                split_node.right = n
            n.parent = split_node
            continue

        return root


def main():
    f = open("input.txt", "r")
    line = f.readline().strip()
    root = create_node(line)

    for line in f:
        root = Node(root, create_node(line.strip()))
        root = reduce_snail_number(root)

    print(root.magnitude())


if __name__ == '__main__':
    main()

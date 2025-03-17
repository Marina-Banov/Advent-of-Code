class Tree:
    def __init__(self, data, times):
        self.children = []
        self.data = data
        self.times = times

    def get_all_nodes_with_name(self, data, children):
        if self.data == data:
            children.append(self)
        for child in self.children:
            child.get_all_nodes_with_name(data, children)
        return children

    def print_tree(self, level=0):
        print("   " * level, self.times, self.data)
        for child in self.children:
            child.print_tree(level + 1)

    def calc_sum(self):
        node_sum = 1
        for child in self.children:
            node_sum += child.times * child.calc_sum()
        return node_sum


def part_one(lines):
    rules = ["shiny gold"]
    for rule in rules:
        for line in lines:
            if rule in line:
                new = ' '.join(line.split()[:2])
                if new not in rules:
                    rules.append(new)
    return len(rules) - 1


def part_two(lines):
    root = Tree("shiny gold", 1)
    rules = ["shiny gold"]
    for rule in rules:
        for line in lines:
            words = line.split()
            if rule == ' '.join(words[:2]):
                nodes = root.get_all_nodes_with_name(rule, [])
                i = 4
                while i < len(words):
                    new = ' '.join(words[i + 1:i + 3])
                    for n in nodes:
                        if words[i] != "no" and next((x for x in n.children if x.data == new), None) is None:
                            n.children.append(Tree(new, int(words[i])))
                    rules.append(new)
                    i += 4
    # root.print_tree()
    return root.calc_sum() - 1


def main(fn):
    with open("input", "r") as f:
        lines = f.read().strip().split("\n")
    return fn(lines)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

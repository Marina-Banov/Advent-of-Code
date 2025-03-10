def add_element(j, n):
    try:
        count[j] += n
    except KeyError as e:
        count[j] = n


class PolymerPairs():
    def __init__(self, name, count, children=[]):
        self.name = name
        self.count = count
        self.children = children

    def __repr__(self):
        return f"{self.name}({self.count}) -> [{self.children[0]}, {self.children[1]}]"


f = open("input.txt", 'r')
polymer = f.readline().strip()

polymer_pairs = []
for j in range(len(polymer)-1):
    name = polymer[j] + polymer[j+1]
    try:
        [p for p in polymer_pairs if p.name == name][0].count += 1
    except Exception as e:
        polymer_pairs.append(PolymerPairs(name, 1))

f.readline()
rules = []

while True:
    line = f.readline().strip()
    if line == "":
        break
    name, insertion = line.split(" -> ")
    children = [name[0]+insertion, insertion+name[1]]
    pair = [p for p in polymer_pairs if p.name == name]

    if len(pair) == 0:
        polymer_pairs.append(PolymerPairs(name, 0, children))
    else:
        pair[0].children = children

for i in range(40):
	# copy all polymers by value
    new_polymer_pairs = [PolymerPairs(p.name, p.count, p.children) for p in polymer_pairs]

    for j in range(len(polymer_pairs)):
        if polymer_pairs[j].count == 0:
            continue
        children = [p for p in new_polymer_pairs if p.name in polymer_pairs[j].children]
        children[0].count += polymer_pairs[j].count
        children[1].count += polymer_pairs[j].count
        new_polymer_pairs[j].count -= polymer_pairs[j].count

    polymer_pairs = new_polymer_pairs

count = {}
for p in polymer_pairs:
    if p.count == 0:
        continue
    add_element(p.name[0], p.count/2)
    add_element(p.name[1], p.count/2)

print(max(count.values()) - min(count.values()))

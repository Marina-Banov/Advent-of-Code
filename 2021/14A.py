def add_element(j):
    try:
        count[j] += 1
    except KeyError as e:
        count[j] = 1


f = open("input.txt", 'r')
polymer = f.readline().strip()
count = {}

for j in polymer:
    add_element(j)

f.readline()
rules = []

while True:
    line = f.readline().strip()
    if line == "":
        break
    pair, insertion = line.split(" -> ")
    rules.append((pair[0], insertion, pair[1]))

for i in range(10):
    new_polymer = polymer[0]
    for j in range(len(polymer)-1):
        (_, two, three) = [tup for tup in rules if tup[0] == polymer[j] and tup[2] == polymer[j+1]][0]
        add_element(two)
        new_polymer += two + three
    polymer = new_polymer

print(max(count.values()) - min(count.values()))

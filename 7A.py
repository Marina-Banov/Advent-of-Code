lines = open("input.txt", "r").read().strip().split('\n')
rules = ['shiny gold']

for rule in rules:
    for line in lines:
        if rule in line:
            new = " ".join(line.split()[:2])
            if new not in rules:
                rules.append(new)

print(len(rules)-1)

f = open("input.txt", 'r')

count = 0
for line in f:
	numbers = (line.strip().split(" | ")[1]).split()
	for n in numbers:
		if len(n) in [2, 3, 4, 7]:
			count += 1

print(count)

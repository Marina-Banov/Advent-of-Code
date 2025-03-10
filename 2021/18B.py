algorithm = __import__("18A")


f = open("input.txt", 'r').readlines()
numbers = [algorithm.create_node(line) for line in f]
res = 0
for i in range(len(numbers)):
	for j in range(len(numbers)):
		if i == j:
			continue
		pair = algorithm.Node(numbers[i], numbers[j])
		res = max(res, (algorithm.reduce_snail_number(pair)).magnitude())
		numbers[i] = algorithm.create_node(f[i])
		numbers[j] = algorithm.create_node(f[j])

print(res)

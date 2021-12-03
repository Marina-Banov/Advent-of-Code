f = open("input.txt", "r")

n = f.readline().strip()
zeros = []
ones = []
for bit in n:
    if bit == '0':
        zeros.append(1)
        ones.append(0)
    else:
        zeros.append(0)
        ones.append(1)

while len(n) > 0:
    n = f.readline().strip()
    for i in range(len(n)):
        if n[i] == '0':
            zeros[i] += 1
        else:
            ones[i] += 1

gamma = ''
epsilon = ''
for i in range(len(zeros)):
	if zeros[i] > ones[i]:
		gamma += '0'
		epsilon += '1'
	else:
		gamma += '1'
		epsilon += '0'
print(int(gamma, 2) * int(epsilon, 2))

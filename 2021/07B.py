f = open("input.txt", "r")
positions = list(map(int, f.readline().strip().split(',')))
avg = int(sum(positions) / len(positions))
res = 0
for i in positions:
	diff = abs(i - avg)
	res += diff * (diff + 1) / 2
print(int(res))

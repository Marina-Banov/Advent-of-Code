f = open("input.txt", "r")
positions = list(map(int, f.readline().strip().split(',')))
positions.sort()
mod = positions[int(len(positions)/2)]
res = 0
for i in positions:
	res += abs(i - mod)
print(res)

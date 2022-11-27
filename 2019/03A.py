f = open("input.txt", 'r')
directions = { 'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1) }

wire = f.readline().strip().split(',')
pos = (0, 0)
points = set()
for i in wire:
    for j in range(1, int(i[1:]) + 1):
        pos = tuple(map(sum, zip(pos, directions[i[0]])))
        points.update([pos])

min_res = 99999999
wire = f.readline().strip().split(",")
pos = (0, 0)
for i in wire:
    for j in range(1, int(i[1:]) + 1):
        pos = tuple(map(sum, zip(pos, directions[i[0]])))
        if pos in points:
            min_res = min(min_res, abs(pos[0]) + abs(pos[1]))

print(min_res)

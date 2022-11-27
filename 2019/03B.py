f = open("input.txt", 'r')
directions = { 'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1) }

wire = f.readline().strip().split(',')
pos = (0, 0)
points = set()
n_steps = 0
steps_a = {}
for i in wire:
    for j in range(1, int(i[1:]) + 1):
        pos = tuple(map(sum, zip(pos, directions[i[0]])))
        n_steps += 1
        points.update([pos])
        steps_a[str(pos)] = n_steps

min_res = 99999999
wire = f.readline().strip().split(",")
pos = (0, 0)
n_steps = 0
for i in wire:
    for j in range(1, int(i[1:]) + 1):
        pos = tuple(map(sum, zip(pos, directions[i[0]])))
        n_steps += 1
        if pos in points:
            min_res = min(min_res, n_steps + steps_a[str(pos)])

print(min_res)

import math


f = open("input.txt", 'r')
estimate = int(f.readline().strip())
buses = list(map(int, filter(lambda a: a != 'x', f.readline().strip().split(','))))
min_estimate = math.inf
min_bus = 0
for bus in buses:
    if (estimate // bus + 1) * bus < min_estimate:
        min_estimate = (estimate // bus + 1) * bus
        min_bus = bus
print((min_estimate - estimate) * min_bus)

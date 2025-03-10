def get_range(stringy_boi):
    start = int(stringy_boi.split('-')[0])
    end = int(stringy_boi.split('-')[1])
    return (start, end)


f = open("input.txt", 'r').readlines()
min_r = 1000
max_r = 0

i = 0
while f[i] != "\n":
    range_borders = f[i].strip().split(": ")[1].split(" or ")
    r1, r2 = get_range(range_borders[0]), get_range(range_borders[1])
    min_r = min(min_r, r1[0], r2[0])
    max_r = max(max_r, r1[1], r2[1])
    i += 1

i += 5
sum_invalid = 0
while i < len(f):
    line = list(map(int, f[i].strip().split(',')))
    for el in line:
        if el < min_r or el > max_r:
            sum_invalid += el
    i += 1

print(sum_invalid)

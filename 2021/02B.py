f = open("input.txt", 'r')
horizontal = 0
aim = 0
depth = 0
while True:
    try:
        direction, value = f.readline().strip().split()
        if direction == "forward":
            horizontal += int(value)
            depth += int(value) * aim
        elif direction == "up":
            aim -= int(value)
        else:
            aim += int(value)
    except Exception as e:
        break
print(horizontal * depth)
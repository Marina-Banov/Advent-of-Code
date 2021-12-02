f = open("input.txt", "r")
horizontal = 0
depth = 0
while True:
    try:
        direction, value = f.readline().strip().split()
        if direction == 'forward':
        	horizontal += int(value)
        elif direction == 'up':
        	depth -= int(value)
        else:
        	depth += int(value)
    except Exception as e:
        break
print(horizontal * depth)

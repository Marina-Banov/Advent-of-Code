def forward(length):
    if r == 0:
        move_x(length)
    if r == 1:
        move_y(length)
    if r == 2:
        move_x(-length)
    if r == 3:
        move_y(-length)


def rotate(angle):
    global r
    r = (r + int(angle / 90)) % 4


def move_x(length):
    global x
    x += length


def move_y(length):
    global y
    y += length


f = open("input.txt", 'r')
x = 0
y = 0
r = 0
while True:
    instruction = f.readline().strip()
    if instruction == "":
        print(abs(x) + abs(y))
        break
    if instruction[0] == 'E':
        move_x(int(instruction[1:]))
    elif instruction[0] == 'S':
        move_y(int(instruction[1:]))
    elif instruction[0] == 'W':
        move_x(-int(instruction[1:]))
    elif instruction[0] == 'N':
        move_y(-int(instruction[1:]))
    elif instruction[0] == 'F':
        forward(int(instruction[1:]))
    elif instruction[0] == 'R':
        rotate(int(instruction[1:]))
    elif instruction[0] == 'L':
        rotate(360-int(instruction[1:]))

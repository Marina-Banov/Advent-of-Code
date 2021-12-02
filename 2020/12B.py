def forward(times):
    global x, y
    x += times * wx
    y += times * wy


def rotate(angle):
    global wx, wy
    for i in range(int(angle / 90)):
        tmp = wx
        wx = -1 * wy
        wy = tmp


def move_wx(length):
    global wx
    wx += length


def move_wy(length):
    global wy
    wy += length


f = open("input.txt", "r")
x = 0
y = 0
wx = 10
wy = -1
while True:
    instruction = f.readline().strip()
    if instruction == '':
        print(abs(x) + abs(y))
        break
    if instruction[0] == 'E':
        move_wx(int(instruction[1:]))
    elif instruction[0] == 'S':
        move_wy(int(instruction[1:]))
    elif instruction[0] == 'W':
        move_wx(-int(instruction[1:]))
    elif instruction[0] == 'N':
        move_wy(-int(instruction[1:]))
    elif instruction[0] == 'F':
        forward(int(instruction[1:]))
    elif instruction[0] == 'R':
        rotate(int(instruction[1:]))
    elif instruction[0] == 'L':
        rotate(360-int(instruction[1:]))

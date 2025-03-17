def forward_one(length, x, y, r):
    if r == 0:
        x = move_x_or_y(length, x)
    elif r == 1:
        y = move_x_or_y(length, y)
    elif r == 2:
        x = move_x_or_y(-length, x)
    elif r == 3:
        y = move_x_or_y(-length, y)
    return x, y, r


def forward_two(length, x, y, wx, wy):
    return x + length * wx, y + length * wy


def rotate_one(angle, r):
    return (r + int(angle / 90)) % 4


def rotate_two(angle, wx, wy):
    for i in range(int(angle / 90)):
        tmp = wx
        wx = -1 * wy
        wy = tmp
    return wx, wy


def move_x_or_y(length, x_or_y):
    return x_or_y + length


def part_one(instruction, x, y, r, *_):
    if instruction[0] == 'E':
        x = move_x_or_y(int(instruction[1:]), x)
    elif instruction[0] == 'S':
        y = move_x_or_y(int(instruction[1:]), y)
    elif instruction[0] == 'W':
        x = move_x_or_y(-int(instruction[1:]), x)
    elif instruction[0] == 'N':
        y = move_x_or_y(-int(instruction[1:]), y)
    elif instruction[0] == 'F':
        x, y, r = forward_one(int(instruction[1:]), x, y, r)
    elif instruction[0] == 'R':
        r = rotate_one(int(instruction[1:]), r)
    elif instruction[0] == 'L':
        r = rotate_one(360 - int(instruction[1:]), r)
    return x, y, r, None, None


def part_two(instruction, x, y, _, wx, wy):
    if instruction[0] == 'E':
        wx = move_x_or_y(int(instruction[1:]), wx)
    elif instruction[0] == 'S':
        wy = move_x_or_y(int(instruction[1:]), wy)
    elif instruction[0] == 'W':
        wx = move_x_or_y(-int(instruction[1:]), wx)
    elif instruction[0] == 'N':
        wy = move_x_or_y(-int(instruction[1:]), wy)
    elif instruction[0] == 'F':
        x, y = forward_two(int(instruction[1:]), x, y, wx, wy)
    elif instruction[0] == 'R':
        wx, wy = rotate_two(int(instruction[1:]), wx, wy)
    elif instruction[0] == 'L':
        wx, wy = rotate_two(360-int(instruction[1:]), wx, wy)
    return x, y, None, wx, wy


def main(fn):
    x = 0
    y = 0
    r = 0
    wx = 10
    wy = -1
    with open("input", "r") as f:
        while True:
            instruction = f.readline().strip()
            if instruction == "":
                break
            x, y, r, wx, wy = fn(instruction, x, y, r, wx, wy)
    return abs(x) + abs(y)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

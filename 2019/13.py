from enum import Enum

day9 = __import__("09")


class TileType(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


def part_one(ints):
    p = day9.Program(ints, None)
    p.run()
    return p.res[2::3].count(TileType.BLOCK.value)


def part_two(_):
    return


def main(fn):
    with open("input", "r") as f:
        ints = list(map(int, f.readline().strip().split(',')))
    return fn(ints)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

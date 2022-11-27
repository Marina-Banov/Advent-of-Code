from enum import Enum
day9 = __import__("09A")


class TileType(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


def main():
    f = open("input.txt", 'r')
    ints = list(map(int, f.readline().strip().split(',')))
    p = day9.Program(ints, None)
    p.run()
    print(p.res[2::3].count(TileType.BLOCK.value))


if __name__ == "__main__":
    main()

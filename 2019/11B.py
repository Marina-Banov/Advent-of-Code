day11 = __import__("11A")


def main():
    f = open("input.txt", 'r')
    ints = list(map(int, f.readline().strip().split(',')))
    tiles = [[0 for i in range(100)] for j in range(100)]
    tiles[50][50] = 1
    p = day11.Program(ints, tiles)
    p.run()

    white_tiles = [(i, j) for j in range(len(p.inputs)) for i, val in enumerate(p.inputs[j]) if val == 1]
    min_x = min(tile[1] for tile in white_tiles)
    min_y = min(tile[0] for tile in white_tiles)
    max_x = max(tile[1] for tile in white_tiles)
    max_y = max(tile[0] for tile in white_tiles)

    res = [['#' if (i, j) in white_tiles else ' ' for i in range(min_y, max_y+1)] for j in range(min_x, max_x+1)]
    res = map(list, zip(*res))
    for row in res:
        print("".join(row))


if __name__ == "__main__":
    main()

def achieved_bingo(array):
    if len(array) < 5:
        return False

    for i in range(5):
        row = [i*5, i*5+1, i*5+2, i*5+3, i*5+4]
        if all(elem in array for elem in row):
            return True

        col = [i, i+5, i+10, i+15, i+20]
        if all(elem in array for elem in col):
            return True

    return False


def get_bingo_scores(f, drawn):
    n_bytes = 76
    bingo_scores = []

    while True:
        chunk = f.read(n_bytes)
        if chunk == "":
            break
        board = list(map(int, chunk.strip().split()))
        marked_tiles = []

        for idx, item in enumerate(drawn):
            try:
                bingo_tile = board.index(item)
                board[bingo_tile] = None
                marked_tiles.append(bingo_tile)
                if achieved_bingo(marked_tiles):
                    bingo_scores.append((idx, sum(filter(None, board))))
                    break
            except Exception as e:
                continue

    return bingo_scores


if __name__ == "__main__":
    f = open("input.txt", 'r')
    drawn = list(map(int, f.readline().strip().split(',')))
    idx, _sum = min(get_bingo_scores(f, drawn))
    print(drawn[idx] * _sum)

from utils import find_all_in_matrix, distance_manhattan


def part_one():
    return 2 - 1


def part_two():
    return 1_000_000 - 1


def expand(i, j, insert_rows, insert_cols, n):
    if i >= insert_rows[0]:
        i += n * ([r for r, v in enumerate(insert_rows) if v <= i][-1] + 1)
    if j >= insert_cols[0]:
        j += n * ([c for c, v in enumerate(insert_cols) if v <= j][-1] + 1)
    return i, j


def main(n):
    with open("input.txt", "r") as f:
        image = [list(l.strip()) for l in f.readlines()]
    insert_rows = [i for i, row in enumerate(image) if all([el == "." for el in row])]
    insert_cols = [j for j in range(len(image[0])) if all([row[j] == "." for row in image])]
    galaxies = [
        expand(gi, gj, insert_rows, insert_cols, n())
        for gi, gj in find_all_in_matrix("#", image)
    ]
    apsp = [[distance_manhattan(a, b) for a in galaxies] for b in galaxies]
    return sum([
        sum([apsp[i][j] for i in range(len(apsp)) if i < j])
        for j in range(len(apsp))
    ])


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

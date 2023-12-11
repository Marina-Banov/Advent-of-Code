def part_one():
    return 2 - 1


def part_two():
    return 1_000_000 - 1


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def expand(matrix, insert_rows, insert_cols, i, j, n):
    if i >= insert_rows[0]:
        i += n * ([r for r, v in enumerate(insert_rows) if v <= i][-1] + 1)
    if j >= insert_cols[0]:
        j += n * ([c for c, v in enumerate(insert_cols) if v <= j][-1] + 1)
    return i, j


def find_all_in_matrix(element, matrix):
    found = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                found.append((i, j))
    return found


def main(n):
    with open("input.txt", "r") as f:
        image = [list(l.strip()) for l in f.readlines()]
    insert_rows = [i for i, row in enumerate(image) if all([el == "." for el in row])]
    insert_cols = [j for j in range(len(image[0])) if all([row[j] == "." for row in image])]
    galaxies = [
        expand(image, insert_rows, insert_cols, *g, n())
        for g in find_all_in_matrix("#", image)
    ]
    apsp = [[manhattan(a, b) for a in galaxies] for b in galaxies]
    return sum([
        sum([apsp[i][j] for i in range(len(apsp)) if i < j])
        for j in range(len(apsp))
    ])


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

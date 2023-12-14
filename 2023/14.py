from utils import find_all_in_matrix, in_range, matrix_to_s


def tilt_direction(matrix, d):
    steps = {
        "N": (-1, 0), "W": (0, -1), "S": (1, 0), "E": (0, 1)
    }
    loop = {
        "N": ((len(matrix),), (len(matrix[0]),)),
        "W": ((len(matrix),), (len(matrix[0]),)),
        "S": ((len(matrix)-1, -1, -1), (len(matrix[0]),)),
        "E": ((len(matrix),), (len(matrix[0])-1, -1, -1)),
    }
    for i in range(*loop[d][0]):
        for j in range(*loop[d][1]):
            if matrix[i][j] != "O":
                continue
            r, c = i, j
            r_step, c_step = steps[d]
            while in_range(r + r_step, c + c_step, len(matrix), len(matrix[0])) \
                and matrix[r + r_step][c + c_step] == ".":
                matrix[r + r_step][c + c_step] = "O"
                matrix[r][c] = "."
                r += r_step
                c += c_step


def total_load(platform):
    return sum([len(platform) - i for i, _ in find_all_in_matrix("O", platform)])


def part_one(platform):
    tilt_direction(platform, "N")
    return total_load(platform)


def part_two(platform):
    s = matrix_to_s(platform)
    r = total_load(platform)
    caches = [(s, r)]
    for i in range(1, 1_000_000_000):
        tilt_direction(platform, "N")
        tilt_direction(platform, "W")
        tilt_direction(platform, "S")
        tilt_direction(platform, "E")
        s = matrix_to_s(platform)
        r = total_load(platform)
        if (s, r) in caches:
            break
        caches.append((s, r))
    found = caches.index((s, r))
    return caches[found + (1_000_000_000 - found) % (i - found)][1]


def main(tilt):
    with open("input.txt", "r") as f:
        platform = [list(l.strip()) for l in f.readlines()]
    return tilt(platform)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

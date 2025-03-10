from utils import find_in_matrix, tuple_sum


def part_one():
    return 64


def part_two():
    return 26_501_365


def is_step_allowed(matrix, cur, diff, visited):
    vi, vj = tuple_sum(cur, diff)
    mi, mj = vi % len(matrix), vj % len(matrix[0])
    return (vi, vj) not in visited and matrix[mi][mj] != "#"


def adjacent(matrix, row, col, visited):
    di = [-1, 1,  0, 0]
    dj = [ 0, 0, -1, 1]
    return [
        tuple_sum((row, col), (di[d], dj[d])) for d in range(len(di))
        if is_step_allowed(matrix, (row, col), (di[d], dj[d]), visited)
    ]


def main(n):
    with open("input.txt", "r") as f:
        matrix = [list(line.strip()) for line in f.readlines()]
    ui, uj = find_in_matrix("S", matrix)
    to_visit = [(ui, uj)]
    even = set()
    odd = set()
    prev = set()
    for i in range(n() + 1):
        if i % 2:
            odd.update(to_visit)
        else:
            even.update(to_visit)
        visit_next = set()
        for ui, uj in to_visit:
            visit_next.update(adjacent(matrix, ui, uj, prev))
        prev = set(to_visit)
        to_visit = list(visit_next)
    return len(odd if n() % 2 else even)


if __name__ == "__main__":
    print(main(part_one))
    # print(main(part_two))

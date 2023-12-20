from utils import is_inside_polygon, traverse, trim_polygon, tuple_sum


def update_cols_rows(d, n, n_rows, n_cols):
    if d == "R":
        n_cols[2] += n
        n_cols[1] = max(n_cols[1], n_cols[2])
    elif d == "L":
        n_cols[2] -= n
        n_cols[0] = min(n_cols[0], n_cols[2])
    elif d == "U":
        n_rows[2] -= n
        n_rows[0] = min(n_rows[0], n_rows[2])
    else:
        n_rows[2] += n
        n_rows[1] = max(n_rows[1], n_rows[2])


def part_one(lines):
    n_rows = [0, 0, 0]
    n_cols = [0, 0, 0]
    for d, n, _ in lines:
        update_cols_rows(d, int(n), n_rows, n_cols)
    return n_rows[:2], n_cols[:2]


def part_two(lines):
    n_rows = [0, 0, 0]
    n_cols = [0, 0, 0]
    for _, _, c in lines:
        d = "RDLU"[int(c[-2])]
        n = int(c[2:-2], 16)
        update_cols_rows(d, n, n_rows, n_cols)
    return n_rows[:2], n_cols[:2]


def is_step_allowed(matrix, cur, diff, **_):
    vi, vj = tuple_sum(cur, diff)
    return not matrix[vi][vj]


def main(parse_input):
    with open("input.txt", "r") as f:
        lines = [line.strip().split() for line in f.readlines()]
    n_rows, n_cols = parse_input(lines)
    i, j = -n_rows[0], -n_cols[0]
    lagoon = [[False for _ in range(n_cols[1]+j+1)] for _ in range(n_rows[1]+i+1)]
    lagoon[0][0] = True

    edges = []
    for d, n, _ in lines:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for _ in range(int(n)):
            lagoon[i][j] = True
            i, j = tuple_sum((i, j), directions["DURL".index(d)])
            edges.append((i, j))
    new_edges = trim_polygon(edges)

    trace = []
    for i in range(1, len(lagoon)):
        for j in range(1, len(lagoon[0])):
            if (i, j) not in edges and is_inside_polygon((i, j), new_edges):
                trace = traverse(lagoon, i, j, dfs=False, is_step_allowed=is_step_allowed)
                break
        if len(trace) > 0:
            break

    return len(trace) + len(edges)


if __name__ == "__main__":
    print(main(part_one))
    # print(main(part_two))

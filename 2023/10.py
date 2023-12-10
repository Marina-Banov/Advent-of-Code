def part_one(trace):
    return len(trace) // 2


def part_two(trace):
    return


def in_range(i, j, max_rows, max_cols):
    return 0 <= i < max_rows and 0 <= j < max_cols


def adjacent(matrix, row, col):
    allowed = {
        "S": "UDLR",
        "|": "UD",
        "-": "LR",
        "L": "UR",
        "J": "UL",
        "7": "DL",
        "F": "DR",
    }
    _next = {
        "U": "|7FS",
        "D": "|LJS",
        "L": "-LFS",
        "R": "-J7S",
    }
    di = [-1, 1,  0, 0]
    dj = [ 0, 0, -1, 1]
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    return sorted([
        (row + di[d], col + dj[d]) for d in range(4)
        if in_range(row + di[d], col + dj[d], n_rows, n_cols)
        and "UDLR"[d] in allowed[matrix[row][col]]
        and matrix[row + di[d]][col + dj[d]] in _next["UDLR"[d]]
    ], key=lambda v: "S|-LJ7F".index(matrix[v[0]][v[1]]))


def dfs(matrix, ui, uj):
    visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    stack = [(ui, uj)]
    trace = []
    while len(stack):
        ui, uj = stack.pop()
        trace.append((ui, uj))
        if matrix[ui][uj] == "S" and len(trace) > 1:
            break
        visited[ui][uj] = True
        for vi, vj in adjacent(matrix, ui, uj):
            if not visited[vi][vj] or matrix[vi][vj] == "S":
                stack.append((vi, vj))
    return trace


def find_in_matrix(element, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                return i, j


def main(res):
    with open("input.txt", "r") as f:
        sketch = [list(l.strip()) for l in f.readlines()]
    start_i, start_j = find_in_matrix("S", sketch)
    trace = dfs(sketch, start_i, start_j)
    return res(trace)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

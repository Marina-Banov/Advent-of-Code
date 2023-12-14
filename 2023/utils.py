DIGITS_MAP = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
}


def count_chars(s):
    cc = {c: s.count(c) for c in set(s)}
    return sorted(cc.items(), key=lambda x: -x[1])


def in_range(i, j, max_rows, max_cols):
    return 0 <= i < max_rows and 0 <= j < max_cols


def adjacent(matrix, row, col, diagonally=False, is_step_allowed=lambda *_: True, sort_key=lambda *_: True):
    if diagonally:
        di = [-1, -1, -1,  0, 0,  1, 1, 1]
        dj = [-1,  0,  1, -1, 1, -1, 0, 1]
    else:
        # UDLR
        di = [-1, 1,  0, 0]
        dj = [ 0, 0, -1, 1]
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    return sorted([
        (row + di[d], col + dj[d]) for d in range(len(di))
        if in_range(row + di[d], col + dj[d], n_rows, n_cols)
        and is_step_allowed(matrix[row][col], d, matrix[row + di[d]][col + dj[d]])
    ], key=lambda v: sort_key(matrix[v[0]][v[1]]))


def dfs(matrix, ui, uj, continue_cond=lambda *_: True, break_cond=lambda *_: False, **kwargs):
    visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    stack = [(ui, uj)]
    trace = []
    while len(stack):
        ui, uj = stack.pop()
        if visited[ui][uj] and continue_cond(matrix, ui, uj):
            continue
        trace.append((ui, uj))
        if break_cond(matrix, ui, uj, trace):
            break
        visited[ui][uj] = True
        for vi, vj in adjacent(matrix, ui, uj, **kwargs):
            if not visited[vi][vj]:
                stack.append((vi, vj))
    return trace


def find_in_matrix(element, matrix):
    return find_all_in_matrix(element, matrix)[0]


def find_all_in_matrix(element, matrix):
    found = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                found.append((i, j))
    return found


def distance_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def matrix_to_s(matrix):
    res = []
    for row in matrix:
        res.append("".join(row))
    return "".join(res)


def print_s_matrix(matrix):
    for row in matrix:
        print("".join(row))


def diff_letters(a, b):
    return sum(a[i] != b[i] for i in range(len(a)))

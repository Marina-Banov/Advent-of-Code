DIGITS_MAP = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
}
DIRECTIONS = "UDLR"


def count_chars(s):
    cc = {c: s.count(c) for c in set(s)}
    return sorted(cc.items(), key=lambda x: -x[1])


def in_range(i, j, max_rows, max_cols):
    return 0 <= i < max_rows and 0 <= j < max_cols


def adjacent(
    matrix, row, col,
    diagonally=False,
    is_step_allowed=lambda **_: True,
    sort_key=lambda *_: True,
    **kwargs,
):
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
        (row + di[d], col + dj[d], d) for d in range(len(di))
        if in_range(row + di[d], col + dj[d], n_rows, n_cols)
        and is_step_allowed(
            matrix=matrix,
            cur=(row, col),
            step=d,
            diff=(di[d], dj[d]),
            **kwargs,
        )
    ], key=lambda v: sort_key(matrix[v[0]][v[1]]))


def traverse(
    matrix, ui, uj,
    dfs=True,
    break_cond=lambda *_: False,
    **kwargs,
):
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    to_visit = [(ui, uj)]
    trace = []
    while len(to_visit):
        ui, uj = to_visit.pop() if dfs else to_visit.pop(0)
        if visited[ui][uj]:
            continue
        trace.append((ui, uj))
        if break_cond(matrix, ui, uj, trace):
            break
        visited[ui][uj] = True
        for vi, vj, _ in adjacent(matrix, ui, uj, **kwargs):
            if not visited[vi][vj]:
                to_visit.append((vi, vj))
    return trace


def traverse_direction_aware(
    matrix, ui, uj, direction,
    dfs=True,
    break_cond=lambda *_: False,
    **kwargs,
):
    visited = [[[False] * 4 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    direction = DIRECTIONS.index(direction)
    to_visit = [(ui, uj, direction)]
    trace = set()
    while len(to_visit):
        ui, uj, direction = to_visit.pop() if dfs else to_visit.pop(0)
        if visited[ui][uj][direction]:
            continue
        trace.add((ui, uj))
        if break_cond(matrix, ui, uj, trace):
            break
        visited[ui][uj][direction] = True
        for vi, vj, d in adjacent(matrix, ui, uj, direction=direction, **kwargs):
            if not visited[vi][vj][d]:
                to_visit.append((vi, vj, d))
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


def tuple_diff(a, b):
    return a[0] - b[0], a[1] - b[1]


def tuple_sum(a, b):
    return a[0] + b[0], a[1] + b[1]


def trim_polygon(polygon):
    first = 0
    prev = 0
    same_i, same_j = False, False
    del_indices = []
    for i in range(1, len(polygon)):
        if polygon[i][0] == polygon[prev][0]:
            if same_j:
                del_indices.extend(list(range(first+1, prev)))
                first = i-1
            same_i = True
            same_j = False
        else:
            if same_i:
                del_indices.extend(list(range(first+1, prev)))
                first = i-1
            same_j = True
            same_i = False
        prev = i
    del_indices.extend(list(range(first+1, prev+1)))
    return [p for i, p in enumerate(polygon) if i not in del_indices]


def is_inside_polygon(point, polygon, trim=False):
    if point in polygon:
        return False
    if trim:
        polygon = trim_polygon(polygon)

    def is_left(p, s, e):
        return (e[0] - s[0]) * (p[1] - s[1]) - (e[1] - s[1]) * (p[0] - s[0])

    wn = 0
    for i in range(len(polygon)):
        if polygon[i-1][1] <= point[1]:
            if polygon[i][1] > point[1] and is_left(polygon[i-1], polygon[i], point) > 0: 
                wn += 1
        elif polygon[i][1] <= point[1] and is_left(polygon[i-1], polygon[i], point) < 0:
            wn -= 1
    return wn != 0

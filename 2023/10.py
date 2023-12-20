from utils import DIRECTIONS, find_in_matrix, is_inside_polygon, traverse, trim_polygon


def part_one(_, trace):
    return len(trace) // 2


def part_two(matrix, trace):
    new_trace = trim_polygon(trace)
    return sum([
        1 for j in range(len(matrix[0])) for i in range(len(matrix))
        if (i, j) not in trace and is_inside_polygon((i, j), new_trace)
    ])


def break_cond(matrix, ui, uj, trace):
    return matrix[ui][uj] == "S" and len(trace) > 1


def is_step_allowed(matrix, cur, step, diff, **_):
    allowed_steps = {
        "S": "UDLR",
        "|": "UD", "-": "LR", "L": "UR",
        "J": "UL", "7": "DL", "F": "DR",
    }
    allowed_next = {
        "U": "|7FS", "D": "|LJS",
        "L": "-LFS", "R": "-J7S",
    }
    row, col = cur
    di, dj = diff
    return DIRECTIONS[step] in allowed_steps[matrix[row][col]] \
        and matrix[row + di][col + dj] in allowed_next[DIRECTIONS[step]]


def main(res):
    with open("input.txt", "r") as f:
        sketch = [list(l.strip()) for l in f.readlines()]
    start_i, start_j = find_in_matrix("S", sketch)
    trace = traverse(
        sketch, start_i, start_j,
        break_cond=break_cond,
        is_step_allowed=is_step_allowed,
        sort_key=lambda el: "S|-JL7F".index(el),
    )
    return res(sketch, trace)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

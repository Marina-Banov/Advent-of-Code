from utils import DIRECTIONS, find_in_matrix, traverse


def part_one(trace):
    return len(trace) // 2


def part_two(trace):
    return


def is_start(matrix, ui, uj):
    return matrix[ui][uj] == "S"


def break_cond(matrix, ui, uj, trace):
    return is_start(matrix, ui, uj) and len(trace) > 1


def is_step_allowed(cur, step, _next, **_):
    allowed_steps = {
        "S": "UDLR",
        "|": "UD", "-": "LR", "L": "UR",
        "J": "UL", "7": "DL", "F": "DR",
    }
    allowed_next = {
        "U": "|7FS", "D": "|LJS",
        "L": "-LFS", "R": "-J7S",
    }
    return DIRECTIONS[step] in allowed_steps[cur] and _next in allowed_next[DIRECTIONS[step]]


def main(res):
    with open("input.txt", "r") as f:
        sketch = [list(l.strip()) for l in f.readlines()]
    start_i, start_j = find_in_matrix("S", sketch)
    trace = traverse(
        sketch, start_i, start_j,
        continue_cond=is_start,
        break_cond=break_cond,
        is_step_allowed=is_step_allowed,
        sort_key=lambda el: "S|-JL7F".index(el),
    )
    return res(trace)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

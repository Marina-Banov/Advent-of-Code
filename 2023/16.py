from utils import DIRECTIONS, traverse_direction_aware


def is_step_allowed(matrix, cur, direction, step, **_):
    allowed_steps = {
        #        U     D     L     R
        ".":  [ "U",  "D",  "L",  "R"],
        "|":  [ "U",  "D", "UD", "UD"],
        "-":  ["LR", "LR",  "L",  "R"],
        "/":  [ "R",  "L",  "D",  "U"],
        "\\": [ "L",  "R",  "U",  "D"],
    }
    c = matrix[cur[0]][cur[1]]
    return DIRECTIONS[step] in allowed_steps[c][direction]


def part_one(grid, ui=0, uj=0, direction="R"):
    return len(traverse_direction_aware(
        grid, ui, uj,
        dfs=False,
        direction=direction,
        is_step_allowed=is_step_allowed
    ))


def part_two(grid):
    res = 0
    for col in range(len(grid[0])):
        res = max(res, part_one(grid, 0, col, "D"))
    #     res = max(res, part_one(grid, len(grid)-1, col, "U"))
    # for row in range(len(grid)):
    #     res = max(res, part_one(grid, row, 0, "R"))
    #     res = max(res, part_one(grid, row, len(grid[0])-1, "L"))
    return res


def main(res):
    with open("input.txt", "r") as f:
        grid = [list(l.strip()) for l in f.readlines()]
    return res(grid)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

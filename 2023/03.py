from utils import traverse


def get_part_numbers(trace, schematic):
    trace.sort()
    part_numbers = []
    p = []
    for i, j in trace:
        if not schematic[i][j].isdigit():
            continue
        if len(p) == 0 or (i == p[-1][0] and j == p[-1][1] + 1):
            p.append((i, j))
        else:
            part_numbers.append(int("".join([schematic[i][j] for i, j in p])))
            p = [(i, j)]
    part_numbers.append(int("".join([schematic[i][j] for i, j in p])))
    return part_numbers


def part_one(trace, schematic):
    if all(schematic[i][j].isdigit() for i, j in trace):
        return 0
    return sum(get_part_numbers(trace, schematic))


def part_two(trace, schematic):
    if "*" not in [schematic[i][j] for i, j in trace]:
        return 0
    part_numbers = get_part_numbers(trace, schematic)
    return part_numbers[0] * part_numbers[1] if len(part_numbers) == 2 else 0


def is_not_dot(_next, **_):
    return _next != "."


def main(sum_el):
    with open("input.txt", "r") as f:
        schematic = [list(l.strip()) for l in f.readlines()]
    n_rows = len(schematic)
    n_cols = len(schematic[0])
    visited = [[False for _ in range(n_rows)] for _ in range(n_cols)]
    res = 0
    for row in range(n_rows):
        for col in range(n_cols):
            if not schematic[row][col].isdigit() or visited[row][col]:
                continue
            trace = traverse(
                schematic, row, col,
                diagonally=True,
                is_step_allowed=is_not_dot,
            )
            for ti, tj in trace:
                visited[ti][tj] = True
            res += sum_el(trace, schematic)
    return res


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

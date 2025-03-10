def part_one(supporting, supported_by):
    return sum([
        1 for i in range(1, len(supported_by))
        if all([len(supported_by[s]) > 1 for s in supporting[i]])
    ])


def collapse(i, supporting, supported_by, will_collapse):
    for s in supporting[i]:
        if all([brick in will_collapse for brick in supported_by[s]]):
            will_collapse.add(s)
            will_collapse = collapse(s, supporting, supported_by, will_collapse)
    return will_collapse


def part_two(supporting, supported_by):
    res = 0
    for i in range(1, len(supported_by)):
        if not all([len(supported_by[s]) > 1 for s in supporting[i]]):
            will_collapse = collapse(i, supporting, supported_by, {i})
            will_collapse.remove(i)
            res += len(will_collapse)
    return res


def init_diagram(max_n, bricks):
    diagram = [[[0 for _ in range(max_n[2])] for _ in range(max_n[1])] for _ in range(max_n[0])]
    for b, brick in enumerate(bricks):
        for i in range(brick[0][0], brick[1][0]+1):
            for j in range(brick[0][1], brick[1][1]+1):
                for k in range(brick[0][2], brick[1][2]+1):
                    diagram[i][j][k] = b + 1
    return diagram


def fall_cond_x(brick, diagram, z):
    return not any([
        diagram[i][brick[0][1]][brick[0][2]-z]
        for i in range(brick[0][0], brick[1][0]+1)
    ])


def fall_cond_y(brick, diagram, z):
    return not any([
        diagram[brick[0][0]][j][brick[0][2]-z]
        for j in range(brick[0][1], brick[1][1]+1)
    ])


def fall_cond_z(brick, diagram, z):
    return not diagram[brick[0][0]][brick[0][1]][brick[0][2]-z]


def should_fall(brick, diagram, fall_condition):
    z = 1
    while brick[0][2]-z >= 1 and fall_condition(brick, diagram, z):
        z += 1
    return z - 1


def fall(bricks, diagram):
    # bricks always span over 1 dimension
    fall_conditions = [fall_cond_x, fall_cond_y, fall_cond_z]
    max_z = 0
    for brick in bricks:
        di = [i for i in range(3) if brick[0][i] != brick[1][i]]
        di = 2 if not len(di) else di[0]
        fall_step = should_fall(brick, diagram, fall_conditions[di])
        if not fall_step:
            continue
        for i in range(brick[0][0], brick[1][0]+1):
            for j in range(brick[0][1], brick[1][1]+1):
                for k in range(brick[0][2], brick[1][2]+1):
                    diagram[i][j][k-fall_step] = diagram[i][j][k]
                    diagram[i][j][k] = 0
        brick[0][2] -= fall_step
        brick[1][2] -= fall_step


def get_structure(bricks, diagram):
    supporting = [set() for _ in range(len(bricks)+1)]
    supported_by = [set() for _ in range(len(bricks)+1)]
    for b, brick in enumerate(bricks):
        for i in range(brick[0][0], brick[1][0]+1):
            for j in range(brick[0][1], brick[1][1]+1):
                supporting[b+1].add(diagram[i][j][brick[1][2]+1])
        supporting[b+1].discard(0)
        for s in supporting[b+1]:
            supported_by[s].add(b+1)
    return supporting, supported_by


def main(res):
    max_n = [0, 0, 0]
    bricks = []
    with open("input.txt", "r") as f:
        while True:
            line = f.readline().strip()
            if line == "":
                break
            brick = [list(map(int, part.split(","))) for part in line.split("~")]
            bricks.append(brick)
            max_n = [max(n, brick[1][dim]) for dim, n in enumerate(max_n)]
    max_n = [n + 1 for n in max_n]
    bricks.sort(key=lambda brick: brick[0][2])
    diagram = init_diagram(max_n, bricks)
    fall(bricks, diagram)
    supporting, supported_by = get_structure(bricks, diagram)
    return res(supporting, supported_by)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

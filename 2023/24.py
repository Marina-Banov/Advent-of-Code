from utils import tuple_sum, tuple_diff


def intersect_2d(h1, h2, r1, r2):
    p1, p2 = h1["p"][:2], tuple_sum(h1["p"][:2], h1["v"][:2])
    p3, p4 = h2["p"][:2], tuple_sum(h2["p"][:2], h2["v"][:2])
    a1, a2 = -h1["v"][0], -h1["v"][1]
    b1, b2 = -h2["v"][0], -h2["v"][1]
    det = a1 * b2 - a2 * b1
    if det == 0:
        return False
    c1, c2 = p1[0]*p2[1] - p1[1]*p2[0], p3[0]*p4[1] - p3[1]*p4[0]
    x = (c1 * b1 - a1 * c2) / det
    y = (c1 * b2 - a2 * c2) / det
    if tuple_diff(p1, (x, y))[0] * a1 < 0 or tuple_diff(p3, (x, y))[0] * b1 < 0:
        return False
    return r1 <= x <= r2 and r1 <= y <= r2


def part_one(hailstones):
    crossed = 0
    for i, h1 in enumerate(hailstones):
        for h2 in hailstones[i+1:]:
            crossed += intersect_2d(h1, h2, 200_000_000_000_000, 400_000_000_000_000)
    return crossed


def part_two(hailstones):
    return 0


def main(res):
    with open("input.txt", "r") as f:
        lines = [line.strip().split(" @ ") for line in f.readlines()]
        hailstones = [{
            "p": list(map(int, line[0].split(","))),
            "v": list(map(int, line[1].split(","))),
        } for line in lines]
    return res(hailstones)


if __name__ == "__main__":
    print(main(part_one))
    # print(main(part_two))

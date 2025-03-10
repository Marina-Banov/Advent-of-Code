from math import prod


def part_one(game_id, cubes):
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    return game_id if all(cubes[k] <= v for k, v in limits.items()) else 0


def part_two(_, cubes):
    return prod(cubes.values())


def get_cubes(sets):
    cubes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for s in sets:
        colors = s.split(", ")
        for c in colors:
            v, k = c.split(" ")
            cubes[k] = max(int(v), cubes[k])
    return cubes


def main(sum_el):
    res = 0
    with open("input.txt", "r") as f:
        while True:
            line = f.readline().strip()
            if line == "":
                break
            game_id, sets = line.split(": ")
            game_id = int(game_id.split(" ")[1])
            sets = sets.split("; ")
            cubes = get_cubes(sets)
            res += sum_el(game_id, cubes)
    return res


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

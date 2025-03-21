from collections import deque


def part_one(cups):
    for i in range(100):
        popped = [cups[1], cups[2], cups[3]]
        del cups[1]
        del cups[1]
        del cups[1]
        dest = cups[0] - 1 if cups[0] > 1 else 9
        while dest in popped:
            dest -= 1
            if dest == 0:
                dest = 9
        insert_at = cups.index(dest)
        cups.insert(insert_at + 1, popped[0])
        cups.insert(insert_at + 2, popped[1])
        cups.insert(insert_at + 3, popped[2])
        cups.rotate(-1)
    while cups[0] != 1:
        cups.rotate(-1)
    return "".join(map(str, cups))[1:]


def part_two(_cups):
    return


def main(fn):
    with open("input", "r") as f:
        cups = deque(list(map(int, list(f.readline().strip()))))
    return fn(cups)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

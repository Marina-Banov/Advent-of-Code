def part_one(steps):
    _sum = 0

    for step in steps:
        n = 0
        for c in step:
            n += ord(c)
            n *= 17
            n %= 256
        _sum += n

    return _sum


def part_two(steps):
    boxes = [{} for _ in range(256)]

    for step in steps:
        if "=" in step:
            label = step[:-2]
            n = part_one([label])
            boxes[n][label] = int(step[-1])
        else:
            label = step[:-1]
            n = part_one([label])
            if label in boxes[n]:
                del boxes[n][label]

    return sum([
        sum([(i+1) * (j+1) * boxes[i][label] for j, label in enumerate(boxes[i])])
        for i in range(len(boxes))
    ])


def main(res):
    with open("input.txt", "r") as f:
        steps = f.readline().strip().split(",")
    return res(steps)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

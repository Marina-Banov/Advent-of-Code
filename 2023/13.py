from utils import diff_letters


def reflection(pattern, goal_diff=0):
    for i in range(1, len(pattern)):
        diff = 0
        for j in range(i):
            if i + j >= len(pattern):
                break
            diff += diff_letters(pattern[i-j-1], pattern[i+j])
        if diff == goal_diff:
            return i
    return 0


def part_one(h_pattern, v_pattern):
    return reflection(h_pattern) * 100 + reflection(v_pattern)


def part_two(h_pattern, v_pattern):
    return reflection(h_pattern, 1) * 100 + reflection(v_pattern, 1)


def main(reflection_line):
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
    breaks = [i for i in range(len(lines)) if lines[i] == ""]
    breaks.append(len(lines))
    prev = 0
    res = 0
    for i in breaks:
        h_pattern = [tuple(l) for l in lines[prev:i]]
        v_pattern = list(zip(*h_pattern))
        res += reflection_line(h_pattern, v_pattern)
        prev = i + 1
    return res


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

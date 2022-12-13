import json
from functools import cmp_to_key
part_one = __import__("13A")


def main():
    with open("input.txt", 'r') as f:
        lines = [json.loads(l) for l in f.readlines() if l != "\n"]

    lines.append([[2]])
    lines.append([[6]])
    lines.sort(key=cmp_to_key(part_one.get_order))
    print((lines.index([[2]])+1) * (lines.index([[6]])+1))


if __name__ == "__main__":
    main()

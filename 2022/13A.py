import json


def get_order(left, right):
    for i in range(len(left)):
        l = left[i]
        try:
            r = right[i]
        except IndexError:
            return 1

        if isinstance(l, int) and isinstance(r, int):
            if l == r:
                continue
            return -1 if l < r else 1

        if isinstance(l, list) and isinstance(r, list):
            list_order = get_order(l, r)
            if list_order == 0:
                continue
            return list_order

        if isinstance(l, int) and isinstance(r, list):
            return get_order([l], r)

        if isinstance(l, list) and isinstance(r, int):
            return get_order(l, [r])

    return 0 if len(left) == len(right) else -1


def main():
    with open("input.txt", 'r') as f:
        lines = [json.loads(l) for l in f.readlines() if l != "\n"]

    res = 0
    for i in range(0, len(lines), 2):
        if get_order(lines[i], lines[i+1]) < 0:
            res += i//2 + 1
    print(res)


if __name__ == "__main__":
    main()

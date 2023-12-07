def rank_by_type(count_map):
    if len(count_map) == 1:
        return 6
    if len(count_map) == 2:
        return 4 + (count_map[0][1] == 4)
    if len(count_map) == 3:
        return 2 + (count_map[0][1] == 3)
    return 0 + (len(count_map) == 4)


def rank_by_label(s, labels):
    res = 0
    for c in s:
        res = res * len(labels) + labels.index(c)
    return res


def count_chars(s):
    cc = {c: s.count(c) for c in set(s)}
    return sorted(cc.items(), key=lambda x: -x[1])    


def part_one(hand):
    return rank_by_type(count_chars(hand)), rank_by_label(hand, "23456789TJQKA")


def part_two(hand):
    items = dict(count_chars(hand))
    keys = list(items.keys())
    if "J" in keys and len(keys) > 1:
        items[keys[0 + (not keys.index("J"))]] += items["J"]
        del items["J"]
    items = list(items.items())
    return rank_by_type(items), rank_by_label(hand, "J23456789TQKA")


def main(sort_key):
    with open("input.txt", "r") as f:
        hands = [l.strip().split() for l in f.readlines()]
    hands.sort(key=lambda hand: sort_key(hand[0]))
    return sum([int(hand[1]) * (rank + 1) for rank, hand in enumerate(hands)])


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

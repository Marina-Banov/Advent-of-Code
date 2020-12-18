def get_range(stringy_boi):
    start = int(stringy_boi.split('-')[0])
    end = int(stringy_boi.split('-')[1])
    return (start, end)


def read_from_file(f):
    ranges = []
    min_r = 1000
    max_r = 0

    i = 0
    while f[i] != '\n':
        range_borders = f[i].strip().split(': ')[1].split(' or ')
        r1, r2 = get_range(range_borders[0]), get_range(range_borders[1])
        min_r = min(min_r, r1[0], r2[0])
        max_r = max(max_r, r1[1], r2[1])
        ranges.append({
            "name": f[i].strip().split(': ')[0],
            "r1": r1,
            "r2": r2,
            "position": None
        })
        i += 1
    for r in ranges:
        r["position"] = list(range(len(ranges)))

    i += 2
    tickets = [list(map(int, f[i].strip().split(',')))]

    i += 3
    while i < len(f):
        t = list(map(int, f[i].strip().split(',')))
        if all([x > min_r and x < max_r for x in t]):
            tickets.append(t)
        i += 1

    return ranges, tickets


def find_ticket_fields(ranges, tickets):
    ruleset = []
    for t in tickets:
        for i in range(len(ranges)):
            if len(ranges[i]["position"]) == 0:
                continue
            if len(ranges[i]["position"]) == 1:
                number = ranges[i]["position"][0]
                ruleset.append({
                    "name": ranges[i]["name"],
                    "position": number
                })
                for r in ranges:
                    if number in r["position"]:
                        r["position"].remove(number)
            for j in range(len(ranges)):
                r1, r2 = ranges[j]["r1"], ranges[j]["r2"]
                if t[i] not in range(r1[0], r1[1]+1) and t[i] not in range(r2[0], r2[1]+1):
                    ranges[j]["position"].remove(i)

    ranges = sorted(ranges, key=lambda r: len(r["position"]))
    for i in range(len(ruleset), len(ranges)):
        number = ranges[i]["position"][0]
        ruleset.append({
            "name": ranges[i]["name"],
            "position": number
        })
        for j in range(i+1, len(ranges)):
            ranges[j]["position"].remove(number)
    return ruleset


def main():
    ranges, tickets = read_from_file(open("input.txt", "r").readlines())
    ruleset = find_ticket_fields(ranges, tickets)
    indices = [rule["position"] for rule in ruleset if "departure" in rule["name"]]
    res = 1
    for i in indices:
        res *= tickets[0][i]
    print(res)


if __name__ == '__main__':
    main()

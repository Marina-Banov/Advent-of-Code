def get_range(stringy_boi):
    start = int(stringy_boi.split('-')[0])
    end = int(stringy_boi.split('-')[1])
    return start, end


def get_ranges_and_tickets(lines):
    ranges = []
    i = 0
    while lines[i] != "\n":
        range_borders = lines[i].strip().split(": ")[1].split(" or ")
        r1, r2 = get_range(range_borders[0]), get_range(range_borders[1])
        ranges.append({
            "name": lines[i].strip().split(": ")[0],
            "r1": r1,
            "r2": r2,
            "position": None
        })
        i += 1
    for r in ranges:
        r["position"] = list(range(len(ranges)))
    tickets = [list(map(int, lines[i+2].strip().split(',')))]
    tickets.extend([list(map(int, line.strip().split(','))) for line in lines[i+5:]])
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


def filter_tickets(tickets, min_r, max_r):
    valid = []
    invalid = []
    for ticket in tickets:
        if all([min_r < el < max_r for el in ticket]):
            valid.append(ticket)
        else:
            invalid.append(ticket)
    return valid, invalid


def get_min_max_range(ranges):
    min_r = 1000
    max_r = 0
    for r in ranges:
        r1 = r["r1"]
        r2 = r["r2"]
        min_r = min(min_r, r1[0], r2[0])
        max_r = max(max_r, r1[1], r2[1])
    return min_r, max_r


def part_one(ranges, tickets):
    min_r, max_r = get_min_max_range(ranges)
    _, invalid = filter_tickets(tickets, min_r, max_r)
    return sum([sum([el for el in ticket if not min_r <= el <= max_r]) for ticket in invalid])


def part_two(ranges, tickets):
    min_r, max_r = get_min_max_range(ranges)
    valid, _ = filter_tickets(tickets, min_r, max_r)
    ruleset = find_ticket_fields(ranges, valid)
    indices = [rule["position"] for rule in ruleset if "departure" in rule["name"]]
    res = 1
    for i in indices:
        res *= valid[0][i]
    return res


def main(fn):
    with open("input", "r") as f:
        lines = f.readlines()
    ranges, tickets = get_ranges_and_tickets(lines)
    return fn(ranges, tickets)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

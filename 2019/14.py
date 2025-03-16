import math


def produce(rules, el, quantity, surplus=[]):
    reaction = [rule for rule in rules if el in rule.split(" => ")[1]][0]
    components, result = reaction.split(" => ")
    qr, el = result.split()
    qr = int(qr)
    div = math.ceil(quantity / qr)
    mod = (div * qr - quantity)

    # print(f"da bih dobio {quantity} {el}, produceat cu ga {div} puta i ostat ce mi {mod}")
    if mod != 0:
        try:
            i = [f for f in surplus if f["element"] == el][0]
            i["quantity"] += mod
        except IndexError as _:
            surplus.append({"element": el, "quantity": mod})

    if "ORE" in reaction:
        q, e = components.split()
        return [{"element": "ORE", "quantity": int(q) * div}]

    components = components.split(", ")
    res = []
    for c in components:
        q, e = c.split()
        q = div * int(q)

        try:
            i = [f for f in surplus if f["element"] == e][0]
            if i["quantity"] >= q:
                i["quantity"] -= q
                continue
            else:
                q -= i["quantity"]
                i["quantity"] = 0
        except IndexError as _:
            pass

        r = produce(rules, e, q, surplus)
        for n in r:
            try:
                i = [f for f in res if f["element"] == n["element"]][0]
                i["quantity"] += n["quantity"]
            except IndexError as _:
                res.append(n)
    return res


def part_one(rules):
    return produce(rules, "FUEL", 1)[0]["quantity"]


def part_two(rules):
    ore_per_fuel = produce(rules, "FUEL", 1)[0]["quantity"]
    ore_in_stock = 1_000_000_000_000
    create_n = round(ore_in_stock / ore_per_fuel)
    used_ore = produce(rules, "FUEL", create_n)[0]["quantity"]
    return int(create_n * ore_in_stock / used_ore)


def main(fn):
    with open("input", "r") as f:
        rules = [line.strip() for line in f.readlines()]
    return fn(rules)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

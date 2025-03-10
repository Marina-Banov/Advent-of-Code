import math


def produce(el, quantity, surplus=[]):
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
        
        r = produce(e, q, surplus)
        for n in r:
            try:
                i = [f for f in res if f["element"] == n["element"]][0]
                i["quantity"] += n["quantity"]
            except IndexError as _:
                res.append(n)
    return res


f = open("input.txt", 'r')
rules = [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    print(produce("FUEL", 1)[0]["quantity"])

def part_one(line, memory, and_mask, or_mask):
    mem_id = int(line[0][4:-1])
    mem_value = int(line[1]) & and_mask | or_mask
    el = next((el for el in memory if el["mem_id"] == mem_id), None)
    if el:
        el["mem_value"] = mem_value
    else:
        memory.append({
            "mem_id": mem_id,
            "mem_value": mem_value
        })


def part_two(_line, _memory, _and_mask, _or_mask):
    return


def main(fn):
    memory = []
    with open("input", "r") as f:
        mask = f.readline().strip().split(" = ")[1]
        while mask != "":
            or_mask = int(mask.replace('X', '0'), 2)
            and_mask = int(mask.replace('X', '1'), 2)
            while True:
                line = f.readline().strip()
                if line == "":
                    mask = ""
                    break
                line = line.split(" = ")
                if line[0] == "mask":
                    mask = line[1]
                    break
                fn(line, memory, and_mask, or_mask)
    return sum(el["mem_value"] for el in memory)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

f = open("input.txt", 'r')
memory = []
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
print(sum(el["mem_value"] for el in memory))

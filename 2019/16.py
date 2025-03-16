def get_first_n(l, n):
    string = "".join([str(integer) for integer in l[:n]])
    return int(string)


def part_one(input_list):
    for step in range(100):
        output_list = []
        for i in range(len(input_list)):
            r = 0
            j = i
            mult = 1
            while j < len(input_list):
                r += sum(input_list[j:j + i + 1]) * mult
                mult *= -1
                j += (i + 1) * 2
            output_list.append(abs(r) % 10)
        input_list = output_list
    return "".join([str(integer) for integer in output_list[:8]])


def part_two(input_list):
    offset = get_first_n(input_list, 7)
    input_list = (input_list * 10_000)[offset:]
    # Assuming that len(input_list) > offset
    for step in range(100):
        _sum = sum(input_list)
        output_list = [_sum % 10]
        for i in range(1, len(input_list)):
            _sum -= input_list[i - 1]
            output_list.append(_sum % 10)
        input_list = output_list
    return get_first_n(input_list, 8)


def main(fn):
    with open("input", "r") as f:
        input_list = list(map(int, list(f.read())))
    return fn(input_list)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

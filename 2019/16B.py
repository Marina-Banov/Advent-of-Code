def get_first_n(l, n):
    string = "".join([str(integer) for integer in l[:n]])
    return int(string)

input_list = list(map(int, list(open("input.txt", 'r').read())))
offset = get_first_n(input_list, 7)
input_list = (input_list * 10_000)[offset:]

# Assuming that len(input_list) > offset
for step in range(100):
    _sum = sum(input_list)
    output_list = [_sum % 10]
    for i in range(1, len(input_list)):
        _sum -= input_list[i-1]
        output_list.append(_sum % 10)
    input_list = output_list

print(get_first_n(input_list, 8))

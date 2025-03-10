input_list = list(map(int, list(open("input.txt", 'r').read())))

for step in range(100):
    output_list = []
    for i in range(len(input_list)):
        r = 0
        j = i
        mult = 1
        while j < len(input_list):
            r += sum(input_list[j:j+i+1]) * mult
            mult *= -1
            j += (i+1)*2
        output_list.append(abs(r) % 10)
    input_list = output_list
print("".join([str(integer) for integer in output_list[:8]]))

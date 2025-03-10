def bit_criteria(res, condition):
    i = 0

    while len(res) > 1:
        zeros = []
        ones = []

        for line in res:
            if line[i] == '0':
                zeros.append(line)
            else:
                ones.append(line)

        if condition(len(zeros), len(ones)):
            res = zeros
        else:
            res = ones

        i += 1

    return res[0].strip()


lines = open("input.txt", 'r').readlines()
oxy = bit_criteria(lines, lambda a, b: a > b)
co2 = bit_criteria(lines, lambda a, b: a <= b)
print(int(oxy, 2) * int(co2, 2))

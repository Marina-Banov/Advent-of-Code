def analyze_packet(i):
    global res
    v = bits[i:i+3]
    res += int(v, 2)
    i += 3
    type_ = bits[i:i+3]
    i += 3
    if int(type_, 2) == 4:
        while bits[i] == "1":
            i += 5
        i += 5
    else:
        i += 1
        if bits[i-1] == "0":
            length = int(bits[i:i+15], 2)
            i += 15
            limited_length_packets(i, i+length)
            i += length
        else:
            length = int(bits[i:i+11], 2)
            i += 11
            i = number_of_packets(i, length)
    return i


def limited_length_packets(i, limit):
    while i < limit:
        i = analyze_packet(i)
        if bits[i:] == '' or int(bits[i:]) == 0:
            return


def number_of_packets(i, n_):
    for p in range(n_):
        i = analyze_packet(i)
    return i


f = open("input.txt", "r")
n = f.readline().strip()
bits = (bin(int(n, 16))[2:]).zfill(len(n) * 4)
res = 0
limited_length_packets(0, len(bits))
print(res)

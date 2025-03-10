from functools import reduce
import operator


def literal_packet():
    global i
    x = ""
    while bits[i] == "1":
        x += bits[i+1:i+5]
        i += 5
    x += bits[i+1:i+5]
    i += 5
    return int(x, 2)


def operator_packet():
    global i
    i += 1
    if bits[i-1] == "0":
        length = int(bits[i:i+15], 2)
        i += 15
        return limited_length_packets(i+length)
    else:
        length = int(bits[i:i+11], 2)
        i += 11
        return number_of_packets(length)


def analyze_packet():
    global res, i
    v = bits[i:i+3]
    i += 3
    type_ = int(bits[i:i+3], 2)
    i += 3
    if type_ == 4:
        return literal_packet()
    else:
        arr = operator_packet()
        if type_ == 0:
            return sum(arr)
        elif type_ == 1:
            return reduce(operator.mul, arr, 1)
        elif type_ == 2:
            return min(arr)
        elif type_ == 3:
            return max(arr)
        elif type_ == 5:
            return 1 if arr[0] > arr[1] else 0
        elif type_ == 6:
            return 1 if arr[0] < arr[1] else 0
        else:
            return 1 if arr[0] == arr[1] else 0


def limited_length_packets(limit):
    global i
    res = []
    while i < limit:
        res.append(analyze_packet())
        if bits[i:] == "" or int(bits[i:]) == 0:
            return res
    return res


def number_of_packets(n_):
    global i
    res = []
    for p in range(n_):
        res.append(analyze_packet())
    return res


f = open("input.txt", 'r')
n = f.readline().strip()
bits = (bin(int(n, 16))[2:]).zfill(len(n) * 4)
i = 0
print(limited_length_packets(len(bits))[0])

def binary_decode(sequence, lower, n):
    lo = 0
    hi = n
    mid = (lo + hi) // 2
    i = 0

    while lo + 1 < hi:
        if sequence[i] == lower:
            hi = mid
        else:
            lo = mid
        mid = (lo + hi) // 2
        i += 1
    return mid


f = open("input.txt", "r")
min_id = 128 * 8 + 8
max_id = 0
sum_ids = 0
while True:
    b_pass = f.readline().strip()
    if b_pass == '':
        break
    seat_id = binary_decode(b_pass[:7], 'F', 128) * 8 + binary_decode(b_pass[7:10], 'L', 8)
    sum_ids += seat_id
    if seat_id > max_id:
        max_id = seat_id
    if seat_id < min_id:
        min_id = seat_id
print((max_id + 1) * max_id // 2 - sum_ids - (min_id - 1) * min_id // 2)

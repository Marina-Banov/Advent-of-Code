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


f = open("input.txt", 'r')
max_id = 0
while True:
    b_pass = f.readline().strip()
    if b_pass == "":
        break
    seat_id = binary_decode(b_pass[:7], 'F', 128) * 8 + binary_decode(b_pass[7:10], 'L', 8)
    if seat_id > max_id:
        max_id = seat_id
print(max_id)

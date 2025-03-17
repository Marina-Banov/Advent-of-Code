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


def part_one(seats):
    max_id = 0
    for b_pass in seats:
        seat_id = binary_decode(b_pass[:7], 'F', 128) * 8 + binary_decode(b_pass[7:10], 'L', 8)
        max_id = max(max_id, seat_id)
    return max_id


def part_two(seats):
    min_id = 128 * 8 + 8
    max_id = 0
    sum_ids = 0
    for b_pass in seats:
        seat_id = binary_decode(b_pass[:7], 'F', 128) * 8 + binary_decode(b_pass[7:10], 'L', 8)
        sum_ids += seat_id
        if seat_id > max_id:
            max_id = seat_id
        if seat_id < min_id:
            min_id = seat_id
    return (max_id + 1) * max_id // 2 - sum_ids - (min_id - 1) * min_id // 2


def main(fn):
    seats = []
    with open("input", "r") as f:
        while True:
            b_pass = f.readline().strip()
            if b_pass == "":
                break
            seats.append(b_pass)
    return fn(seats)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

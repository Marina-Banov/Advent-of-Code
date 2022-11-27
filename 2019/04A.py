start, end = open("input.txt", 'r').readline().strip().split('-')
count = 0

i = int(start)
while i < int(end):
    digits = list(str(i))
    factor = 10000
    flag = False
    for j in range(5):
        if digits[j] > digits[j+1]:
            i = int((i + factor) / factor) * factor
            flag = True
            break
        factor = int(factor / 10)
    if flag:
        continue
    if any([digit == digits[j+1] for j, digit in enumerate(digits) if j < 5]):
        count += 1
    i += 1
print(count)

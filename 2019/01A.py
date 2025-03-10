f = open("input.txt", 'r')

res = 0
while True:
    try:
        m = int(f.readline().strip())
        res += int(m / 3) - 2
    except Exception as e:
        break
print(res)

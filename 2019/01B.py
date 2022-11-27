f = open("input.txt", 'r')

res = 0
while True:
    try:
        m = int(f.readline().strip())
        m = int(m / 3) - 2
        while m > 0:
            res += m
            m = int(m / 3) - 2
    except Exception as e:
        break
print(res)

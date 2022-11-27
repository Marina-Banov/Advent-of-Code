f = open("input.txt", 'r')
count = 0
prev = None
while True:
    try:
        curr = int(f.readline().strip())
        if prev is not None and prev < curr:
            count += 1
        prev = curr
    except Exception as e:
        break
print(count)

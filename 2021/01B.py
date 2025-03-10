f = open("input.txt", 'r')
values = f.readlines()
count = 0
prev = None
for i in range(len(values)-2):
    a = int(values[i].strip())
    b = int(values[i+1].strip())
    c = int(values[i+2].strip())
    curr = a + b + c
    if prev is not None and prev < curr:
        count += 1
    prev = curr
print(count)

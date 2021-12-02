def resolve(q):
    i = 0
    while i < len(q):
        if q[i] == '+':
            q[i] = q[i-1] + q[i+1]
            q.pop(i-1)
            q.pop(i)
            i -= 1
        i += 1

    res = q[0]
    i = 1
    while i < len(q):
        res *= q[i+1]
        i += 2
    return res


def create_req(string, i):
    q = []
    while i < len(string):
        if string[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            q.append(int(string[i]))
        elif string[i] in ['+', '*']:
            q.append(string[i])
        elif string[i] == '(':
            q_, i = create_req(string, i+1)
            q.append(resolve(q_))
        elif string[i] == ')':
            return q, i
        i += 1
    return q, i


f = open("input.txt", "r")
total = 0

while True:
    string = f.readline().strip()
    if len(string) == 0:
        break
    q, i = create_req(string, 0)
    total += resolve(q)

print(total)

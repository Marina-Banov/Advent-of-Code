def part_one(q):
    res = q[0]
    i = 1
    while i < len(q):
        if q[i] == '+':
            res += q[i+1]
        elif q[i] == '*':
            res *= q[i+1]
        i += 2
    return res


def part_two(q):
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


def create_req(string, i, fn):
    q = []
    while i < len(string):
        if string[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            q.append(int(string[i]))
        elif string[i] in ['+', '*']:
            q.append(string[i])
        elif string[i] == '(':
            q_, i = create_req(string, i+1, fn)
            q.append(fn(q_))
        elif string[i] == ')':
            return q, i
        i += 1
    return q, i


def main(fn):
    total = 0
    with open("input", "r") as f:
        while True:
            string = f.readline().strip()
            if len(string) == 0:
                break
            q, i = create_req(string, 0, fn)
            total += fn(q)
    return total


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

charges = list(map(int, open("input.txt", "r").read().strip().split()))
charges.append(0)
charges = sorted(charges)
ones = 0
threes = 1
for i in range(len(charges)):
    try:
        if charges[i] + 1 == charges[i+1]:
            ones += 1
        elif charges[i] + 3 == charges[i+1]:
            threes += 1
    except Exception as e:
        print(ones * threes)

import sys

f = open("input.txt", 'r')
less = []
more = []
exact = 0
while True:
    try:
        n = int(f.readline().strip())
    except Exception as e:
        break
    if n > 1010:
        more.append(n)
    elif n < 1010:
        less.append(n)
    else:
        exact += 1

if exact == 2:
    print(1010*1010)
    sys.exit()

for lt in sorted(less):
    for mt in sorted(more, reverse=True):
        if lt + mt == 2020:
            print(lt*mt)
            sys.exit
        elif lt + mt < 2020:
            break

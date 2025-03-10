day2 = __import__("02A")


def main():
    f = open("input.txt", 'r')
    ints = list(map(int, f.readline().strip().split(',')))
    
    pairs = []
    for i in range(len(ints)-1):
        for j in range(i, len(ints)):
            pairs.append((i, j))
    
    while True:
        a, b = pairs.pop()
        p = day2.Program(ints[:])
        p.ints[1] = a
        p.ints[2] = b
        p.run()
        if p.ints[0] == 19690720:
            print(100 * a + b)
            break


if __name__ == "__main__":
    main()

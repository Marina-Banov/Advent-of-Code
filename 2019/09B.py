day9 = __import__("09A")


def main():
    f = open("input.txt", 'r')
    ints = list(map(int, f.readline().strip().split(',')))
    p = day9.Program(ints, 2)
    p.run()
    print(p.res[0])


if __name__ == "__main__":
    main()

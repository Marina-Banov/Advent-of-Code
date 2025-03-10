def main():
    lines = open("input.txt", 'r').readlines()
    accumulator = 0
    i = 0
    visited = []
    while True:
        line = lines[i].strip().split()
        jump = 1
        if line[0] == "acc":
            accumulator += int(line[1])
        elif line[0] == "jmp":
            jump = int(line[1])
        visited.append(i)
        i += jump
        if i == len(lines) or i in visited:
            break
    print(accumulator)


if __name__ == "__main__":
    main()

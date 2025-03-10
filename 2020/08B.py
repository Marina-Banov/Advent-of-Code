def run_game(lines):
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
        if i == len(lines):
            return (True, accumulator)
        if i in visited:
            return (False, accumulator)


def main():
    lines = open("input.txt", 'r').readlines()
    for i in range(len(lines)):
        line = lines[i].strip().split()
        if line[0] == "acc":
            continue
        lines_cpy = lines[:]
        if line[0] == "nop":
            lines_cpy[i] = "jmp " + line[1]
        else:
            lines_cpy[i] = "nop " + line[1]
        res = run_game(lines_cpy)
        if res[0] is True:
            print(res[1])
            break


if __name__ == "__main__":
    main()

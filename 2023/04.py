def part_one(n_winning):
    return sum([2 ** (n-1) for n in n_winning if n])


def part_two(n_winning):
    for i in range(len(n_winning)-1, -1, -1):
        n_winning[i] += sum(n_winning[i+1 : i+1+n_winning[i]])
    return sum(n_winning) + len(n_winning)


def main(sum_el):
    n_winning = []
    with open("input.txt", "r") as f:
        while True:
            line = f.readline().strip()
            if line == "":
                break
            winning, owned = line.split(": ")[1].split(" | ")
            winning = list(map(int, winning.split()))
            owned = list(map(int, owned.split()))
            n_winning.append(len(set(winning).intersection(owned)))
    return sum_el(n_winning)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

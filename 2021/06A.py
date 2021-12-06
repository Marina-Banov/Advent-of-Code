def main(n_days):
    f = open("input.txt", "r")
    lanternfish = list(map(int,f.readline().strip().split(',')))

    bins = [[day, 0] for day in range(9)]

    for i in range(len(lanternfish)):
        bins[lanternfish[i]][1] += 1

    for i in range(n_days):
        for j in range(9):
            bins[j][0] -= 1
        new_spawns = [k for k in range(9) if bins[k][0] == -1][0]
        restart_cycle = [k for k in range(9) if bins[k][0] == 6][0]
        bins[new_spawns][0] = 8
        bins[restart_cycle][1] += bins[new_spawns][1]

    print(sum([bins[i][1] for i in range(9)]))


if __name__ == '__main__':
    main(80)

def read_cards(f):
    player = []
    f.readline()
    while True:
        n = f.readline().strip()
        if n == "":
            return player
        player.append(int(n))


def calc_score(player):
    score = 0
    for i in range(len(player)):
        score += player[i] * (len(player) - i)
    return score


def main():
    f = open("input.txt", 'r')
    player_one = read_cards(f)
    player_two = read_cards(f)

    while len(player_one) > 0 and len(player_two) > 0:
        one = player_one.pop(0)
        two = player_two.pop(0)
        if one > two:
            player_one.append(one)
            player_one.append(two)
        else:
            player_two.append(two)
            player_two.append(one)

    print(calc_score(player_one if len(player_two) == 0 else player_two))


if __name__ == "__main__":
    main()

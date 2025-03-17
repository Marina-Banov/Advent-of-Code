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


def part_one(player_one, player_two):
    while len(player_one) > 0 and len(player_two) > 0:
        one = player_one.pop(0)
        two = player_two.pop(0)
        if one > two:
            player_one.append(one)
            player_one.append(two)
        else:
            player_two.append(two)
            player_two.append(one)
    return 1 if len(player_two) == 0 else 2


def part_two(player_one, player_two):
    rounds = [player_one[:]]
    while len(player_one) > 0 and len(player_two) > 0:
        one = player_one.pop(0)
        two = player_two.pop(0)
        if len(player_one) >= one and len(player_two) >= two:
            winner = part_two(player_one[:one], player_two[:two])
        else:
            winner = 1 if one > two else 2
        if winner == 1:
            player_one.append(one)
            player_one.append(two)
        else:
            player_two.append(two)
            player_two.append(one)
        if player_one in rounds:
            return 1
        else:
            rounds.append(player_one[:])
    return 1 if len(player_two) == 0 else 2


def main(fn):
    with open("input", "r") as f:
        player_one = read_cards(f)
        player_two = read_cards(f)
    winner = fn(player_one, player_two)
    return calc_score(player_one if winner == 1 else player_two)


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

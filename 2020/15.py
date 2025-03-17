def part_one():
    return 2020


def part_two():
    return 0  # 30000000


def run_game(numbers, n):
    game = []
    for i in range(len(numbers)):
        game.append({
            "value": numbers[i],
            "last_turn": i + 1
        })
    spoken = 0
    turn = len(numbers) + 1
    while turn < n:
        occured = next((el for el in game if el["value"] == spoken), None)
        if occured:
            spoken = turn - occured["last_turn"]
            occured["last_turn"] = turn
        else:
            game.append({
                "value": spoken,
                "last_turn": turn
            })
            spoken = 0
        turn += 1
    return spoken


def main(fn):
    with open("input", "r") as f:
        numbers = list(map(int, f.readline().strip().split(',')))
    return run_game(numbers, fn())


if __name__ == "__main__":
    print(main(part_one))
    print(main(part_two))

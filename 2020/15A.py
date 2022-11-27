f = open("input.txt", 'r')
numbers = list(map(int, f.readline().strip().split(',')))
game = []
for i in range(len(numbers)):
    game.append({
        "value": numbers[i],
        "last_turn": i+1
    })
spoken = 0
turn = len(numbers)+1
while turn < 2020:
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
print(spoken)

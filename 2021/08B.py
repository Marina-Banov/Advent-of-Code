def modify_potential(potential, indices, word, exception):
    for p in indices:
        potential[p] = [x for x in word if x not in exception]


def get_mapped_segments(train_data):
    potential = [LETTERS for i in range(7)]

    # number 1 defines potential values for indices 1 and 2
    modify_potential(potential, [1, 2], train_data[0], '')
    # remove those values from other indices
    modify_potential(potential, [0, 3, 4, 5, 6], potential[0], potential[1])

    # number 7 defines value for index 0
    modify_potential(potential, [0], train_data[1], potential[1])
    # remove that value from other indices
    modify_potential(potential, [3, 4, 5, 6], potential[3], potential[0])

    # number 4 defines potential values for indices 5 and 6
    modify_potential(potential, [5, 6], train_data[2], potential[1])
    # remove those values from other indices
    modify_potential(potential, [3, 4], potential[3], potential[5])

    for i in [6, 7, 8]:
        diff_letter = [l for l in LETTERS if l not in train_data[i]][0]
        if diff_letter in potential[1]:
            potential[1] = [diff_letter]
            potential[2].remove(diff_letter)
        elif diff_letter in potential[3]:
            potential[4] = [diff_letter]
            potential[3].remove(diff_letter)
        elif diff_letter in potential[5]:
            potential[6] = [diff_letter]
            potential[5].remove(diff_letter)

    return [p[0] for p in potential]


f = open("input.txt", "r")
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
MAP_DIGITS = [
    [0, 1, 2, 3, 4, 5],         #
    [1, 2],                     #
    [0, 1, 3, 4, 6],            #      0000
    [0, 1, 2, 3, 6],            #     5    1
    [1, 2, 5, 6],               #     5    1
    [0, 2, 3, 5, 6],            #      6666
    [0, 2, 3, 4, 5, 6],         #     4    2
    [0, 1, 2],                  #     4    2
    [0, 1, 2, 3, 4, 5, 6],      #      3333
    [0, 1, 2, 3, 5, 6],         #
]
res = 0 

for line in f:
    train, test = line.strip().split(' | ')
    train = train.split()
    train.sort(key = lambda p: len(p))
    mapped_segments = get_mapped_segments(train)

    number = 0
    multiplier = 1000
    for word in test.split():
        digit = MAP_DIGITS.index([idx for idx, val in enumerate(mapped_segments) if val in word])
        number += digit * multiplier
        multiplier /= 10
    res += number

print(res)

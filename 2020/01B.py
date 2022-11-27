import sys

f = open("input.txt", 'r')

numbers = list(map(int, [line.strip() for line in f.readlines()]))

for x in range(len(numbers)):
    for y in range(x+1, len(numbers)):
        for z in range(y+1, len(numbers)):
            if numbers[x] + numbers[y] + numbers[z] == 2020:
                print(numbers[x] * numbers[y] * numbers[z])
                sys.exit()

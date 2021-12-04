f = open("input.txt", "r")
drawn = list(map(int, f.readline().strip().split(',')))
idx, _sum = max(__import__('04A').get_bingo_scores(f, drawn))
print(drawn[idx] * _sum)

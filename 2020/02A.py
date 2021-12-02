f = open("input.txt", "r")
valid = 0

while True:
    n = f.readline().strip()
    if n == '':
        break
    min_appearance, password = n.split("-")
    max_appearance, letter, password = password.split(" ")
    letter = letter.strip(":")
    if password.count(letter) <= int(max_appearance) and password.count(letter) >= int(min_appearance):
        valid += 1

print(valid)
